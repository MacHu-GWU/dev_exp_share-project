# -*- coding: utf-8 -*-

"""
我有 1 台服务器.

Pricing Fact:

- 1 WCU = 1KB.
- 1 RCU = 4KB. 如果是 eventual consistent read 则减半.
- 1M WCU = $1.25
- 1M RCU = $0.25
- $0.25 per GM/Month (对于我们的 App 来说可以忽略不计)

Workload Fact:

- 平均 30 秒测量一次, 1 天测量 2880 次.
- 每次测量的数据大小大约在 0.25 KB, 但是要消耗 1 WCU.
- 平均 15 分钟查询一次最近 3 小时的服务器的测量数据, 1 天查询 96 次.
- 3 小时的数据大约是 3 * 60 * 2 = 360 个 item, 一共 90KB, 也就是消耗 90 WCU.

Cost:

- Write: 1 天测量 2880 次乘以每次消耗 1 WCU, 共计 2880 WCU. 也就是 1.25 * 2880 / 1000000 = $0.0036/天, 等于 $0.108/月.
- Read: 1 天查询 96 次乘以每次消耗 90 WCU, 共计 8640 WCU. 也就是 0.25 * 8640 / 1000000 / 2 = $0.00108/天, 等于 $0.0648/月.
- 也就是为了测量一台服务器的使用情况需要花费 0.1656 美元/月. 6 台服务器也就是大约一个月 $1.
    一个 RDS db.t4g.small 空转 5 小时大约就是 0.16 美元, 所以是有必要测量的.
"""

import polars as pl
import pynamodb_mate.api as pm
from datetime import datetime

class Measurement(pm.Model):
    class Meta:
        table_name = "measurement"
        region = "us-east-1"
        billing_mode = pm.constants.PAY_PER_REQUEST_BILLING_MODE

    key = pm.UnicodeAttribute(hash_key=True)
    ts = pm.UTCDateTimeAttribute(range_key=True)
    cpu_usage = pm.NumberAttribute()
    memory_usage = pm.NumberAttribute()

    @classmethod
    def query_between(
        cls,
        key: str,
        start_time: datetime,
        end_time: datetime,
    ):
        return cls.iter_query(
            hash_key=key,
            range_key_condition=cls.ts.between(start_time, end_time),
        )

    @classmethod
    def list_to_df(
        cls,
        items: list,
    ) -> pl.DataFrame:
        print(cls.get_attributes())
        cols = list(cls.get_attributes())
        cols.remove("key")
        cols.remove("ts")
        cols = ["key", "ts"] + cols
        df = pl.DataFrame(
            [item.attribute_values for item in items],
            schema=cols,
        )
        return df


if __name__ == "__main__":
    import random

    import moto
    from datetime import timedelta, timezone
    from rich import print as rprint
    from boto_session_manager import BotoSesManager

    def get_utc_now():
        return datetime.utcnow().replace(tzinfo=timezone.utc)

    mock_aws = moto.mock_aws()
    mock_aws.start()

    bsm = BotoSesManager(region_name="us-east-1")
    print(f"{bsm.aws_account_id = }")
    Measurement.create_table(wait=True)

    start_time = get_utc_now()
    ec2_inst_id = "i-1234567890abcdef0"
    with Measurement.batch_write() as batch:
        for i in range(10):
            measurement = Measurement(
                key=ec2_inst_id,
                ts=start_time + timedelta(seconds=i),
                cpu_usage=random.randint(5, 95),
                memory_usage=random.randint(5, 95),
            )
            batch.save(measurement)

    measurements = Measurement.query_between(
        ec2_inst_id,
        start_time=start_time,
        end_time=start_time + timedelta(seconds=10),
    ).all()

    rprint([item.attribute_values for item in measurements])

    df = Measurement.list_to_df(items=measurements)

    mock_aws.stop()