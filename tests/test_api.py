# -*- coding: utf-8 -*-

from dev_exp_share import api


def test():
    _ = api


if __name__ == "__main__":
    from dev_exp_share.tests import run_cov_test

    run_cov_test(__file__, "dev_exp_share.api", preview=False)
