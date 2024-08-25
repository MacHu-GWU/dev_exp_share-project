# ==============================================================================
# Consolidated Source Code for jsonpolars
#
# **Purpose**
#
# This document serves as a comprehensive knowledge base for the jsonpolars project,
# enabling GenAI tools to reference the entire codebase efficiently.
#
# **Rationale**
#
# Due to limitations in processing multiple files, this document concatenates
# all source code files into a single, easily accessible format.
#
# **Contents**
#
# - Complete source code from all project files
# - File paths and names preserved as comments before each file's content
#
# Note:
#
# This consolidated view is generated automatically and should be updated
# whenever significant changes are made to the project's source code.
# ==============================================================================

# ==============================================================================
# Below is the source code folder structure:
#
#     jsonpolars/__init__.py
#     jsonpolars/_version.py
#     jsonpolars/api.py
#     jsonpolars/base_dfop.py
#     jsonpolars/base_expr.py
#     jsonpolars/dfop/__init__.py
#     jsonpolars/dfop/aggregation.py
#     jsonpolars/dfop/api.py
#     jsonpolars/dfop/manipulation.py
#     jsonpolars/docs/__init__.py
#     jsonpolars/expr/__init__.py
#     jsonpolars/expr/api.py
#     jsonpolars/expr/column.py
#     jsonpolars/expr/dt.py
#     jsonpolars/expr/function.py
#     jsonpolars/expr/list.py
#     jsonpolars/expr/manipulation.py
#     jsonpolars/expr/string.py
#     jsonpolars/gen_code/__init__.py
#     jsonpolars/gen_code/gen_api.py
#     jsonpolars/paths.py
#     jsonpolars/sentinel.py
#     jsonpolars/tests/__init__.py
#     jsonpolars/tests/dfop_case.py
#     jsonpolars/tests/expr_case.py
#     jsonpolars/tests/helper.py
#     jsonpolars/typehint.py
#     jsonpolars/utils_dfop.py
#     jsonpolars/utils_expr.py
#
# ==============================================================================
# ------------------------------------------------------------------------------
# Start of jsonpolars/__init__.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

"""
Package Description.
"""

from ._version import __version__

__short_description__ = "Package short description."
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__maintainer__ = "Sanhe Hu"
__maintainer_email__ = "husanhe@email.com"
__github_username__ = "MacHu-GWU"

# ------------------------------------------------------------------------------
# End of jsonpolars/__init__.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/_version.py content
# ------------------------------------------------------------------------------
__version__ = "0.1.1"

if __name__ == "__main__":  # pragma: no cover
    print(__version__)

# ------------------------------------------------------------------------------
# End of jsonpolars/_version.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/api.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from .base_expr import parse_expr
from .expr.api import T_EXPR
from .expr import api as expr
from .base_dfop import parse_dfop
from .dfop.api import T_DFOP
from .dfop import api as dfop

# ------------------------------------------------------------------------------
# End of jsonpolars/api.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/base_dfop.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

"""
Base DataFrame operation.
"""

import typing as T
import enum
import dataclasses

from .vendor.better_dataclasses import DataClass

from .sentinel import NOTHING, REQUIRED, OPTIONAL

if T.TYPE_CHECKING:  # pragma: no cover
    from .dfop.api import T_DFOP


class DfopEnum(str, enum.Enum):
    """ """

    # Aggregation
    count = "count"
    max = "max"
    max_horizontal = "max_horizontal"
    mean = "mean"
    mean_horizontal = "mean_horizontal"
    median = "median"
    min = "min"
    min_horizontal = "min_horizontal"
    product = "product"
    quantile = "quantile"
    std = "std"
    sum = "sum"
    sum_horizontal = "sum_horizontal"
    var = "var"
    # Attributes
    # Computation
    # Descriptive
    # Export
    # GroupBy
    group_by_agg = "group_by_agg"
    group_by_all = "group_by_all"
    group_by_count = "group_by_count"
    group_by_first = "group_by_first"
    group_by_head = "group_by_head"
    group_by_last = "group_by_last"
    group_by_len = "group_by_len"
    group_by_map_groups = "group_by_map_groups"
    group_by_max = "group_by_max"
    group_by_mean = "group_by_mean"
    group_by_median = "group_by_median"
    group_by_min = "group_by_min"
    group_by_n_unique = "group_by_n_unique"
    group_by_quantile = "group_by_quantile"
    group_by_sum = "group_by_sum"
    group_by_tail = "group_by_tail"
    # Manipulation / selection
    bottom_k = "bottom_k"
    cast = "cast"
    clear = "clear"
    clone = "clone"
    drop = "drop"
    drop_in_place = "drop_in_place"
    drop_nulls = "drop_nulls"
    explode = "explode"
    extend = "extend"
    fill_nan = "fill_nan"
    fill_null = "fill_null"
    filter = "filter"
    gather_every = "gather_every"
    get_column = "get_column"
    get_column_index = "get_column_index"
    get_columns = "get_columns"
    group_by = "group_by"
    group_by_dynamic = "group_by_dynamic"
    head = "head"
    hstack = "hstack"
    insert_column = "insert_column"
    interpolate = "interpolate"
    item = "item"
    iter_columns = "iter_columns"
    iter_rows = "iter_rows"
    iter_slices = "iter_slices"
    join = "join"
    join_asof = "join_asof"
    limit = "limit"
    melt = "melt"
    merge_sorted = "merge_sorted"
    partition_by = "partition_by"
    pipe = "pipe"
    pivot = "pivot"
    rechunk = "rechunk"
    rename = "rename"
    replace_column = "replace_column"
    reverse = "reverse"
    rolling = "rolling"
    row = "row"
    rows = "rows"
    rows_by_key = "rows_by_key"
    sample = "sample"
    select = "select"
    select_seq = "select_seq"
    set_sorted = "set_sorted"
    shift = "shift"
    shrink_to_fit = "shrink_to_fit"
    slice = "slice"
    sort = "sort"
    sql = "sql"
    tail = "tail"
    to_dummies = "to_dummies"
    to_series = "to_series"
    top_k = "top_k"
    transpose = "transpose"
    unique = "unique"
    unnest = "unnest"
    unpivot = "unpivot"
    unstack = "unstack"
    update = "update"
    upsample = "upsample"
    vstack = "vstack"
    with_columns = "with_columns"
    with_columns_seq = "with_columns_seq"
    with_row_count = "with_row_count"
    with_row_index = "with_row_index"
    # Miscellaneous
    # Plot
    # Style


@dataclasses.dataclass
class BaseDfop(DataClass):
    type: str = dataclasses.field(default=REQUIRED)

    def _validate(self):
        for k, v in dataclasses.asdict(self).items():
            if v is REQUIRED:  # pragma: no cover
                raise ValueError(f"Field {k!r} is required for {self.__class__}.")

    def __post_init__(self):
        self._validate()


dfop_enum_to_klass_mapping: T.Dict[str, T.Type["T_DFOP"]] = dict()


def parse_dfop(dct: T.Dict[str, T.Any]) -> "T_DFOP":
    """
    Note: you have to import everything in the :mod:`jsonpolars.dfop` module
    to make this work.
    """
    return dfop_enum_to_klass_mapping[dct["type"]].from_dict(dct)

# ------------------------------------------------------------------------------
# End of jsonpolars/base_dfop.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/base_expr.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import enum
import dataclasses

import polars as pl
from .vendor.better_dataclasses import DataClass

from .sentinel import NOTHING, REQUIRED, OPTIONAL

if T.TYPE_CHECKING:  # pragma: no cover
    from .expr.api import T_EXPR


class ExprEnum(str, enum.Enum):
    # Aggregation
    agg = "agg"
    agg_groups = "agg_groups"
    arg_max = "arg_max"
    arg_min = "arg_min"
    agg_count = "agg_count"
    agg_first = "agg_first"
    agg_implode = "agg_implode"
    agg_last = "agg_last"
    agg_len = "agg_len"
    agg_max = "agg_max"
    agg_mean = "agg_mean"
    agg_median = "agg_median"
    agg_min = "agg_min"
    agg_nan_max = "agg_nan_max"
    agg_nan_min = "agg_nan_min"
    agg_product = "agg_product"
    agg_quantile = "agg_quantile"
    agg_std = "agg_std"
    agg_sum = "agg_sum"
    agg_var = "agg_var"
    # Array
    arr = "arr"
    arr_max = "arr_max"
    arr_min = "arr_min"
    arr_median = "arr_median"
    arr_sum = "arr_sum"
    arr_std = "arr_std"
    arr_to_list = "arr_to_list"
    arr_unique = "arr_unique"
    arr_n_unique = "arr_n_unique"
    arr_var = "arr_var"
    arr_all = "arr_all"
    arr_any = "arr_any"
    arr_sort = "arr_sort"
    arr_reverse = "arr_reverse"
    arr_arg_min = "arr_arg_min"
    arr_arg_max = "arr_arg_max"
    arr_get = "arr_get"
    arr_first = "arr_first"
    arr_last = "arr_last"
    arr_join = "arr_join"
    arr_explode = "arr_explode"
    arr_contains = "arr_contains"
    arr_count_matches = "arr_count_matches"
    arr_to_struct = "arr_to_struct"
    arr_shift = "arr_shift"
    # Binary
    binary = "binary"
    binary_contains = "binary_contains"
    binary_decode = "binary_decode"
    binary_encode = "binary_encode"
    binary_ends_with = "binary_ends_with"
    binary_size = "binary_size"
    binary_starts_with = "binary_starts_with"
    # Boolean
    # Categories
    # Columns / names
    column = "column"
    alias = "alias"
    # Computation
    # Functions
    lit = "lit"
    plus = "plus"
    minus = "minus"
    multiple = "multiple"
    divide = "divide"
    # List
    list = "list"
    list_all = "list_all"
    list_any = "list_any"
    list_drop_nulls = "list_drop_nulls"
    list_arg_max = "list_arg_max"
    list_arg_min = "list_arg_min"
    list_concat = "list_concat"
    list_contains = "list_contains"
    list_count_matches = "list_count_matches"
    list_diff = "list_diff"
    list_eval = "list_eval"
    list_explode = "list_explode"
    list_first = "list_first"
    list_gather = "list_gather"
    list_get = "list_get"
    list_head = "list_head"
    list_join = "list_join"
    list_last = "list_last"
    list_len = "list_len"
    list_max = "list_max"
    list_mean = "list_mean"
    list_median = "list_median"
    list_min = "list_min"
    list_reverse = "list_reverse"
    list_sample = "list_sample"
    list_set_difference = "list_set_difference"
    list_set_intersection = "list_set_intersection"
    list_set_symmetric_difference = "list_set_symmetric_difference"
    list_set_union = "list_set_union"
    list_shift = "list_shift"
    list_slice = "list_slice"
    list_sort = "list_sort"
    list_std = "list_std"
    list_sum = "list_sum"
    list_tail = "list_tail"
    list_to_array = "list_to_array"
    list_to_struct = "list_to_struct"
    list_unique = "list_unique"
    list_n_unique = "list_n_unique"
    list_var = "list_var"
    list_gather_every = "list_gather_every"
    # Manipulation / selection
    append = "append"
    arg_sort = "arg_sort"
    arg_true = "arg_true"
    backward_fill = "backward_fill"
    bottom_k = "bottom_k"
    bottom_k_by = "bottom_k_by"
    cast = "cast"
    ceil = "ceil"
    clip = "clip"
    cut = "cut"
    drop_nans = "drop_nans"
    drop_nulls = "drop_nulls"
    explode = "explode"
    extend_constant = "extend_constant"
    fill_nan = "fill_nan"
    fill_null = "fill_null"
    filter = "filter"
    flatten = "flatten"
    floor = "floor"
    forward_fill = "forward_fill"
    gather = "gather"
    gather_every = "gather_every"
    get = "get"
    head = "head"
    inspect = "inspect"
    interpolate = "interpolate"
    interpolate_by = "interpolate_by"
    limit = "limit"
    lower_bound = "lower_bound"
    pipe = "pipe"
    qcut = "qcut"
    rechunk = "rechunk"
    reinterpret = "reinterpret"
    repeat_by = "repeat_by"
    replace = "replace"
    replace_strict = "replace_strict"
    reshape = "reshape"
    reverse = "reverse"
    rle = "rle"
    rle_id = "rle_id"
    round = "round"
    round_sig_figs = "round_sig_figs"
    sample = "sample"
    shift = "shift"
    shrink_dtype = "shrink_dtype"
    shuffle = "shuffle"
    slice = "slice"
    sort = "sort"
    sort_by = "sort_by"
    tail = "tail"
    to_physical = "to_physical"
    top_k = "top_k"
    top_k_by = "top_k_by"
    upper_bound = "upper_bound"
    where = "where"
    # Meta
    # Miscellaneous
    # Name
    # Operators
    and_ = "and"
    or_ = "or"
    eq = "eq"
    eq_missing = "eq_missing"
    ge = "ge"
    gt = "gt"
    le = "le"
    lt = "lt"
    ne = "ne"
    ne_missing = "ne_missing"
    add = "add"
    floordiv = "floordiv"
    mod = "mod"
    mul = "mul"
    neg = "neg"
    sub = "sub"
    truediv = "truediv"
    pow = "pow"
    xor = "xor"
    # String
    string = "string"
    str_concat = "str_concat"
    str_contains = "str_contains"
    str_contains_any = "str_contains_any"
    str_count_matches = "str_count_matches"
    str_decode = "str_decode"
    str_encode = "str_encode"
    str_ends_with = "str_ends_with"
    str_explode = "str_explode"
    str_extract = "str_extract"
    str_extract_all = "str_extract_all"
    str_extract_groups = "str_extract_groups"
    str_extract_many = "str_extract_many"
    str_find = "str_find"
    str_head = "str_head"
    str_join = "str_join"
    str_json_decode = "str_json_decode"
    str_json_path_match = "str_json_path_match"
    str_len_bytes = "str_len_bytes"
    str_len_chars = "str_len_chars"
    str_pad_end = "str_pad_end"
    str_pad_start = "str_pad_start"
    str_replace = "str_replace"
    str_replace_all = "str_replace_all"
    str_replace_many = "str_replace_many"
    str_reverse = "str_reverse"
    str_slice = "str_slice"
    str_split = "str_split"
    str_split_exact = "str_split_exact"
    str_splitn = "str_splitn"
    str_starts_with = "str_starts_with"
    str_strip_chars = "str_strip_chars"
    str_strip_chars_start = "str_strip_chars_start"
    str_strip_chars_end = "str_strip_chars_end"
    str_strip_prefix = "str_strip_prefix"
    str_strip_suffix = "str_strip_suffix"
    str_strptime = "str_strptime"
    str_tail = "str_tail"
    str_to_date = "str_to_date"
    str_to_datetime = "str_to_datetime"
    str_to_decimal = "str_to_decimal"
    str_to_integer = "str_to_integer"
    str_to_lowercase = "str_to_lowercase"
    str_to_titlecase = "str_to_titlecase"
    str_to_time = "str_to_time"
    str_to_uppercase = "str_to_uppercase"
    str_zfill = "str_zfill"
    # Struct
    struct = "struct"
    struct_field = "struct_field"
    struct_json_encode = "struct_json_encode"
    struct_rename_fields = "struct_rename_fields"
    struct_with_fields = "struct_with_fields"
    # Temporal
    dt = "datetime"
    dt_add_business_days = "dt_add_business_days"
    dt_base_utc_offset = "dt_base_utc_offset"
    dt_cast_time_unit = "dt_cast_time_unit"
    dt_century = "dt_century"
    dt_combine = "dt_combine"
    dt_convert_time_zone = "dt_convert_time_zone"
    dt_date = "dt_date"
    dt_datetime = "dt_datetime"
    dt_day = "dt_day"
    dt_dst_offset = "dt_dst_offset"
    dt_epoch = "dt_epoch"
    dt_hour = "dt_hour"
    dt_is_leap_year = "dt_is_leap_year"
    dt_iso_year = "dt_iso_year"
    dt_microsecond = "dt_microsecond"
    dt_millennium = "dt_millennium"
    dt_millisecond = "dt_millisecond"
    dt_minute = "dt_minute"
    dt_month = "dt_month"
    dt_month_end = "dt_month_end"
    dt_month_start = "dt_month_start"
    dt_nanosecond = "dt_nanosecond"
    dt_offset_by = "dt_offset_by"
    dt_ordinal_day = "dt_ordinal_day"
    dt_quarter = "dt_quarter"
    dt_replace_time_zone = "dt_replace_time_zone"
    dt_round = "dt_round"
    dt_second = "dt_second"
    dt_strftime = "dt_strftime"
    dt_time = "dt_time"
    dt_timestamp = "dt_timestamp"
    dt_to_string = "dt_to_string"
    dt_total_days = "dt_total_days"
    dt_total_hours = "dt_total_hours"
    dt_total_microseconds = "dt_total_microseconds"
    dt_total_milliseconds = "dt_total_milliseconds"
    dt_total_minutes = "dt_total_minutes"
    dt_total_nanoseconds = "dt_total_nanoseconds"
    dt_total_seconds = "dt_total_seconds"
    dt_truncate = "dt_truncate"
    dt_week = "dt_week"
    dt_weekday = "dt_weekday"
    dt_with_time_unit = "dt_with_time_unit"
    dt_year = "dt_year"
    # Window


@dataclasses.dataclass
class BaseExpr(DataClass):
    type: str = dataclasses.field(default=REQUIRED)

    def _validate(self):
        for k, v in dataclasses.asdict(self).items():
            if v is REQUIRED:  # pragma: no cover
                raise ValueError(f"Field {k!r} is required for {self.__class__}.")

    def __post_init__(self):
        self._validate()

    def to_polars(self) -> pl.Expr:
        raise NotImplementedError()


expr_enum_to_klass_mapping: T.Dict[str, T.Type["T_EXPR"]] = dict()


def parse_expr(dct: T.Dict[str, T.Any]) -> "T_EXPR":
    """
    Note: you have to import everything in the :mod:`jsonpolars.expr` module
    to make this work.
    """
    return expr_enum_to_klass_mapping[dct["type"]].from_dict(dct)

# ------------------------------------------------------------------------------
# End of jsonpolars/base_expr.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/dfop/__init__.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-


# ------------------------------------------------------------------------------
# End of jsonpolars/dfop/__init__.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/dfop/aggregation.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..expr import api as expr
from ..base_dfop import DfopEnum, BaseDfop, dfop_enum_to_klass_mapping

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_DFOP
    from ..expr.api import T_EXPR
    from ..typehint import IntoExpr, ColumnNameOrSelector


@dataclasses.dataclass
class Count(BaseDfop):
    """
    https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.count.html
    """

    type: str = dataclasses.field(default=DfopEnum.count.value)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls()

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.count()


dfop_enum_to_klass_mapping[DfopEnum.count.value] = Count


# ------------------------------------------------------------------------------
# End of jsonpolars/dfop/aggregation.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/dfop/api.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
from .manipulation import Select
from .manipulation import Rename
from .manipulation import Drop
from .manipulation import WithColumns
from .manipulation import Head
from .manipulation import Tail
from .manipulation import Sort
from .manipulation import DropNulls
from .aggregation import Count

T_DFOP = T.Union[
    Select,
    Rename,
    Drop,
    WithColumns,
    Head,
    Tail,
    Sort,
    DropNulls,
    Count,
]

# ------------------------------------------------------------------------------
# End of jsonpolars/dfop/api.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/dfop/manipulation.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..expr import api as expr
from .. import utils_expr
from ..base_dfop import DfopEnum, BaseDfop, dfop_enum_to_klass_mapping

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_DFOP
    from ..expr.api import T_EXPR
    from ..typehint import IntoExpr, ColumnNameOrSelector


def _extract_exprs_named_exprs(exprs, named_exprs):
    """
    Used in Select.from_dict and WithColumns.from_dict.
    """
    new_exprs = [utils_expr.to_jsonpolars_into_expr(expr_like) for expr_like in exprs]
    new_named_exprs = {
        name: utils_expr.to_jsonpolars_into_expr(expr_like)
        for name, expr_like in named_exprs.items()
    }
    return new_exprs, new_named_exprs


def _convert_to_exprs_named_exprs(exprs, named_exprs):
    """
    Used in Select.to_polars and WithColumns.to_polars.
    """
    new_exprs = [utils_expr.to_polars_into_expr(expr_like) for expr_like in exprs]
    new_named_exprs = {
        name: utils_expr.to_polars_into_expr(expr_like)
        for name, expr_like in named_exprs.items()
    }
    return new_exprs, new_named_exprs


@dataclasses.dataclass
class Select(BaseDfop):
    """
    https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.select.html
    """

    type: str = dataclasses.field(default=DfopEnum.select.value)
    exprs: T.List["IntoExpr"] = dataclasses.field(default_factory=list)
    named_exprs: T.Dict[str, "IntoExpr"] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        exprs, named_exprs = _extract_exprs_named_exprs(
            dct["exprs"], dct["named_exprs"]
        )
        return cls(exprs=exprs, named_exprs=named_exprs)

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        exprs, named_exprs = _convert_to_exprs_named_exprs(self.exprs, self.named_exprs)
        return df.select(*exprs, **named_exprs)


dfop_enum_to_klass_mapping[DfopEnum.select.value] = Select


@dataclasses.dataclass
class Rename(BaseDfop):
    type: str = dataclasses.field(default=DfopEnum.rename.value)
    mapping: T.Union[T.Dict[str, str], T.Callable[[str], str]] = dataclasses.field(
        default=REQUIRED
    )

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            mapping=dct["mapping"],
        )

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.rename(self.mapping)


dfop_enum_to_klass_mapping[DfopEnum.rename.value] = Rename


@dataclasses.dataclass
class Drop(BaseDfop):
    """
    https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.drop.html
    """

    type: str = dataclasses.field(default=DfopEnum.drop.value)
    columns: T.List["ColumnNameOrSelector"] = dataclasses.field(default=REQUIRED)
    strict: bool = dataclasses.field(default=True)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        columns, _ = _extract_exprs_named_exprs(dct["columns"], {})
        return cls(
            columns=columns,
            strict=dct["strict"],
        )

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        columns, _ = _convert_to_exprs_named_exprs(self.columns, {})
        return df.drop(*columns, strict=self.strict)


dfop_enum_to_klass_mapping[DfopEnum.drop.value] = Drop


@dataclasses.dataclass
class WithColumns(BaseDfop):
    """
    https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.with_columns.html#
    """

    type: str = dataclasses.field(default=DfopEnum.with_columns.value)
    exprs: T.List["IntoExpr"] = dataclasses.field(default_factory=list)
    named_exprs: T.Dict[str, "IntoExpr"] = dataclasses.field(default_factory=dict)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        exprs, named_exprs = _extract_exprs_named_exprs(
            dct["exprs"], dct["named_exprs"]
        )
        return cls(exprs=exprs, named_exprs=named_exprs)

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        exprs, named_exprs = _convert_to_exprs_named_exprs(self.exprs, self.named_exprs)
        return df.with_columns(*exprs, **named_exprs)


dfop_enum_to_klass_mapping[DfopEnum.with_columns.value] = WithColumns


@dataclasses.dataclass
class Head(BaseDfop):
    """
    https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.head.html
    """

    type: str = dataclasses.field(default=DfopEnum.head.value)
    n: int = dataclasses.field(default=5)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(n=dct["n"])

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.head(self.n)


dfop_enum_to_klass_mapping[DfopEnum.head.value] = Head


@dataclasses.dataclass
class Tail(BaseDfop):
    """
    https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.tail.html
    """

    type: str = dataclasses.field(default=DfopEnum.tail.value)
    n: int = dataclasses.field(default=5)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(n=dct["n"])

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.tail(self.n)


dfop_enum_to_klass_mapping[DfopEnum.tail.value] = Tail


@dataclasses.dataclass
class Sort(BaseDfop):
    """
    https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.sort.html#
    """

    type: str = dataclasses.field(default=DfopEnum.sort.value)
    by: T.List["IntoExpr"] = dataclasses.field(default=REQUIRED)
    descending: T.Union[bool, T.List[bool]] = dataclasses.field(default=False)
    nulls_last: T.Union[bool, T.List[bool]] = dataclasses.field(default=False)
    multithreaded: bool = dataclasses.field(default=True)
    maintain_order: bool = dataclasses.field(default=False)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            by=[
                utils_expr.to_jsonpolars_into_expr(expr_like) for expr_like in dct["by"]
            ],
            descending=dct["descending"],
            nulls_last=dct["nulls_last"],
            multithreaded=dct["multithreaded"],
            maintain_order=dct["maintain_order"],
        )

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.sort(
            *[utils_expr.to_polars_into_expr(expr_like) for expr_like in self.by],
            descending=self.descending,
            nulls_last=self.nulls_last,
            multithreaded=self.multithreaded,
            maintain_order=self.maintain_order,
        )


dfop_enum_to_klass_mapping[DfopEnum.sort.value] = Sort


@dataclasses.dataclass
class DropNulls(BaseDfop):
    """
    https://docs.pola.rs/api/python/stable/reference/dataframe/api/polars.DataFrame.drop_nulls.html
    """

    type: str = dataclasses.field(default=DfopEnum.drop_nulls.value)
    subset: T.List["ColumnNameOrSelector"] = dataclasses.field(default=None)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        if dct["subset"] is None:
            subset = None
        else:
            subset, _ = _extract_exprs_named_exprs(dct["subset"], {})
        return cls(subset=subset)

    def to_polars(self, df: pl.DataFrame) -> pl.DataFrame:
        return df.drop_nulls(subset=self.subset)


dfop_enum_to_klass_mapping[DfopEnum.drop_nulls.value] = DropNulls

# ------------------------------------------------------------------------------
# End of jsonpolars/dfop/manipulation.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/docs/__init__.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

doc_data = dict()

# ------------------------------------------------------------------------------
# End of jsonpolars/docs/__init__.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/expr/__init__.py content
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# End of jsonpolars/expr/__init__.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/expr/api.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
from .manipulation import Cast
from .list import List
from .list import ListGet
from .dt import Datetime
from .dt import DatetimeToString
from .string import String
from .string import Split
from .string import StrJoin
from .function import Lit
from .function import Plus
from .function import Minus
from .column import Column
from .column import Alias

T_EXPR = T.Union[
    Cast,
    List,
    ListGet,
    Datetime,
    DatetimeToString,
    String,
    Split,
    StrJoin,
    Lit,
    Plus,
    Minus,
    Column,
    Alias,
]

# ------------------------------------------------------------------------------
# End of jsonpolars/expr/api.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/expr/column.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


@dataclasses.dataclass
class Column(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.column.value)
    name: str = dataclasses.field(default=REQUIRED)

    def to_polars(self) -> pl.Expr:
        return pl.col(self.name)


expr_enum_to_klass_mapping[ExprEnum.column.value] = Column


@dataclasses.dataclass
class Alias(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.alias.value)
    name: str = dataclasses.field(default=REQUIRED)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            name=dct["name"],
            expr=parse_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return self.expr.to_polars().alias(self.name)


expr_enum_to_klass_mapping[ExprEnum.alias.value] = Alias

# ------------------------------------------------------------------------------
# End of jsonpolars/expr/column.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/expr/dt.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


def ensure_datetime(expr: "T_EXPR") -> pl.Expr:
    if isinstance(expr, Datetime):
        return expr.to_polars()
    else:
        return expr.to_polars().dt


@dataclasses.dataclass
class Datetime(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.dt.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(expr=parse_expr(dct["expr"]))

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr)


expr_enum_to_klass_mapping[ExprEnum.dt.value] = Datetime


@dataclasses.dataclass
class DatetimeToString(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.dt_to_string.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    format: str = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            format=dct["format"],
        )

    def to_polars(self) -> pl.Expr:
        return ensure_datetime(self.expr).to_string(format=self.format)


expr_enum_to_klass_mapping[ExprEnum.dt_to_string.value] = DatetimeToString

# ------------------------------------------------------------------------------
# End of jsonpolars/expr/dt.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/expr/function.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR
    from ..typehint import OtherExpr


@dataclasses.dataclass
class Lit(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.lit.value)
    value: T.Any = dataclasses.field(default=REQUIRED)

    def to_polars(self) -> pl.Expr:
        return pl.lit(self.value)


expr_enum_to_klass_mapping[ExprEnum.lit.value] = Lit


def _other_expr_to_polars(other_expr: "OtherExpr"):
    """
    Convert jsonpolars expression to polars expression.

    Example

    >>> _other_expr_to_polars(1)
    1
    >>> _other_expr_to_polars("hello")
    'hello'
    >>> _other_expr_to_polars(Column("col_1"))
    pl.col("col_1")
    """
    if isinstance(other_expr, BaseExpr):
        return other_expr.to_polars()
    else:
        return other_expr


def _parse_other_expr(value) -> "OtherExpr":
    if isinstance(value, dict):
        return parse_expr(value)
    else:
        return value


@dataclasses.dataclass
class Plus(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.plus.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=_parse_other_expr(dct["left"]),
            right=_parse_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) + _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.plus.value] = Plus


@dataclasses.dataclass
class Minus(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.minus.value)
    left: "OtherExpr" = dataclasses.field(default=REQUIRED)
    right: "OtherExpr" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            left=_parse_other_expr(dct["left"]),
            right=_parse_other_expr(dct["right"]),
        )

    def to_polars(self) -> pl.Expr:
        return _other_expr_to_polars(self.left) - _other_expr_to_polars(self.right)


expr_enum_to_klass_mapping[ExprEnum.minus.value] = Minus

# ------------------------------------------------------------------------------
# End of jsonpolars/expr/function.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/expr/list.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


def ensure_list(expr: "T_EXPR") -> pl.Expr:
    if isinstance(expr, List):
        return expr.to_polars()
    else:
        return expr.to_polars().list


@dataclasses.dataclass
class List(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.list.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_list(self.expr)


expr_enum_to_klass_mapping[ExprEnum.list.value] = List


@dataclasses.dataclass
class ListGet(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.list_get.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    index: T.Union[int, "T_EXPR"] = dataclasses.field(default=REQUIRED)
    null_on_oob: bool = dataclasses.field(default=False)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        index = dct["index"]
        if isinstance(index, int):
            pass
        elif isinstance(index, dict):
            index = parse_expr(index)
        else:  # pragma: no cover
            raise ValueError(f"Unknown index type: {index}")
        return cls(
            expr=parse_expr(dct["expr"]),
            index=index,
            null_on_oob=dct["null_on_oob"],
        )

    def to_polars(self) -> pl.Expr:
        expr = ensure_list(self.expr)
        if isinstance(self.index, int):
            index = self.index
        elif isinstance(self.index, BaseExpr):
            index = self.index.to_polars()
        return expr.get(index=index, null_on_oob=self.null_on_oob)


expr_enum_to_klass_mapping[ExprEnum.list_get.value] = ListGet

# ------------------------------------------------------------------------------
# End of jsonpolars/expr/list.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/expr/manipulation.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


@dataclasses.dataclass
class Cast(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.cast.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    dtype: pl.DataType = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            dtype=dct["dtype"],
        )

    def to_polars(self) -> pl.Expr:
        return self.expr.to_polars().cast(self.dtype)


expr_enum_to_klass_mapping[ExprEnum.cast.value] = Cast

# ------------------------------------------------------------------------------
# End of jsonpolars/expr/manipulation.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/expr/string.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl

from ..sentinel import NOTHING, REQUIRED, OPTIONAL
from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from .api import T_EXPR


def ensure_string(expr: "T_EXPR") -> pl.Expr:
    if isinstance(expr, String):
        return expr.to_polars()
    else:
        return expr.to_polars().str


@dataclasses.dataclass
class String(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.string.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
        )

    def to_polars(self) -> pl.Expr:
        return ensure_string(self.expr)


expr_enum_to_klass_mapping[ExprEnum.string.value] = String


@dataclasses.dataclass
class Split(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.str_split.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    by: str = dataclasses.field(default=REQUIRED)
    inclusive: bool = dataclasses.field(default=False)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            by=dct["by"],
            inclusive=dct["inclusive"],
        )

    def to_polars(self) -> pl.Expr:
        expr = ensure_string(self.expr)
        return expr.split(by=self.by, inclusive=self.inclusive)


expr_enum_to_klass_mapping[ExprEnum.str_split.value] = Split


@dataclasses.dataclass
class StrJoin(BaseExpr):
    type: str = dataclasses.field(default=ExprEnum.str_join.value)
    expr: "T_EXPR" = dataclasses.field(default=REQUIRED)
    delimiter: str = dataclasses.field(default="")
    ignore_nulls: bool = dataclasses.field(default=True)

    @classmethod
    def from_dict(cls, dct: T.Dict[str, T.Any]):
        return cls(
            expr=parse_expr(dct["expr"]),
            delimiter=dct.get("delimiter", ""),
            ignore_nulls=dct.get("ignore_nulls", True),
        )

    def to_polars(self) -> pl.Expr:
        return self.expr.to_polars().str.join(
            delimiter=self.delimiter, ignore_nulls=self.ignore_nulls
        )


# Add this class to the expr_enum_to_klass_mapping
expr_enum_to_klass_mapping[ExprEnum.str_join.value] = StrJoin

# ------------------------------------------------------------------------------
# End of jsonpolars/expr/string.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/gen_code/__init__.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-


# ------------------------------------------------------------------------------
# End of jsonpolars/gen_code/__init__.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/gen_code/gen_api.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

"""
自动生成 api.py 模块.
"""

import importlib
import dataclasses

from jinja2 import Template
from jsonpolars.paths import dir_python_lib
from jsonpolars.base_expr import BaseExpr
from jsonpolars.base_dfop import BaseDfop


@dataclasses.dataclass
class Klass:
    module_name: str
    class_name: str


dir_expr = dir_python_lib / "expr"
dir_dfop = dir_python_lib / "dfop"


def gen_expr_api():
    ignore_file = [
        "__init__.py",
        "api.py",
    ]
    ignore_class_name = [
        "BaseExpr",
    ]
    klass_list = list()
    for path in dir_expr.iterdir():
        if path.name.endswith(".py") and path.name not in ignore_file:
            print(f"extract class from {path.name!r} ...")
            module_name = f"jsonpolars.expr.{path.stem}"
            module_content = path.read_text()
            module = importlib.import_module(module_name)
            for var_name, var_value in module.__dict__.items():
                if isinstance(var_value, type) and issubclass(var_value, BaseExpr):
                    if (f"class {var_name}" in module_content) and (
                        var_name not in ignore_class_name
                    ):
                        print(f"  found class {var_name!r}")
                        klass = Klass(
                            module_name=path.stem,
                            class_name=var_name,
                        )
                        klass_list.append(klass)

    path_tpl = dir_python_lib / "gen_code" / "expr_api.jinja"
    tpl = Template(path_tpl.read_text())
    content = tpl.render(klass_list=klass_list)

    path_api = dir_expr / "api.py"
    path_api.write_text(content)


def gen_dfop_api():
    ignore_file = [
        "__init__.py",
        "api.py",
    ]
    ignore_class_name = [
        "BaseDfop",
    ]
    klass_list = list()
    for path in dir_dfop.iterdir():
        if path.name.endswith(".py") and path.name not in ignore_file:
            print(f"extract class from {path.name!r} ...")
            module_name = f"jsonpolars.dfop.{path.stem}"
            module_content = path.read_text()
            module = importlib.import_module(module_name)
            for var_name, var_value in module.__dict__.items():
                if isinstance(var_value, type) and issubclass(var_value, BaseDfop):
                    if (f"class {var_name}" in module_content) and (
                        var_name not in ignore_class_name
                    ):
                        print(f"  found class {var_name!r}")
                        klass = Klass(
                            module_name=path.stem,
                            class_name=var_name,
                        )
                        klass_list.append(klass)

    path_tpl = dir_python_lib / "gen_code" / "dfop_api.jinja"
    tpl = Template(path_tpl.read_text())
    content = tpl.render(klass_list=klass_list)

    path_api = dir_dfop / "api.py"
    path_api.write_text(content)


gen_expr_api()
gen_dfop_api()

# ------------------------------------------------------------------------------
# End of jsonpolars/gen_code/gen_api.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/paths.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from pathlib import Path

dir_python_lib = Path(__file__).absolute().parent
PACKAGE_NAME = dir_python_lib.name

dir_project_root = dir_python_lib.parent

# ------------------------------------------------------------------------------
# Virtual Environment Related
# ------------------------------------------------------------------------------
dir_venv = dir_project_root / ".venv"
dir_venv_bin = dir_venv / "bin"

# virtualenv executable paths
bin_pytest = dir_venv_bin / "pytest"

# test related
dir_htmlcov = dir_project_root / "htmlcov"
path_cov_index_html = dir_htmlcov / "index.html"
dir_unit_test = dir_project_root / "tests"

# ------------------------------------------------------------------------------
# End of jsonpolars/paths.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/sentinel.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import sys


def make_sentinel(name="_MISSING", var_name=None):  # pragma: no cover
    """Creates and returns a new **instance** of a new class, suitable for
    usage as a "sentinel", a kind of singleton often used to indicate
    a value is missing when ``None`` is a valid input.
    Args:
        name (str): Name of the Sentinel
        var_name (str): Set this name to the name of the variable in
            its respective module enable pickleability. Note:
            pickleable sentinels should be global constants at the top
            level of their module.
    >>> make_sentinel(var_name='_MISSING')
    _MISSING
    The most common use cases here in boltons are as default values
    for optional function arguments, partly because of its
    less-confusing appearance in automatically generated
    documentation. Sentinels also function well as placeholders in queues
    and linked lists.
    .. note::
      By design, additional calls to ``make_sentinel`` with the same
      values will not produce equivalent objects.
      >>> make_sentinel('TEST') == make_sentinel('TEST')
      False
      >>> type(make_sentinel('TEST')) == type(make_sentinel('TEST'))
      False
    """

    class Sentinel(object):
        def __init__(self):
            self.name = name
            self.var_name = var_name

        def __repr__(self):
            if self.var_name:
                return self.var_name
            return "%s(%r)" % (self.__class__.__name__, self.name)

        if var_name:

            def __reduce__(self):
                return self.var_name

        def __nonzero__(self):
            return False

        __bool__ = __nonzero__

    if var_name:
        frame = sys._getframe(1)
        module = frame.f_globals.get("__name__")
        if not module or module not in sys.modules:
            raise ValueError(
                "Pickleable sentinel objects (with var_name) can only"
                " be created from top-level module scopes"
            )
        Sentinel.__module__ = module

    return Sentinel()


NOTHING = make_sentinel(name="NOTHING")
REQUIRED = make_sentinel(name="REQUIRED")
OPTIONAL = make_sentinel(name="OPTIONAL")


def resolve_kwargs(
    _mapper: T.Optional[T.Dict[str, str]] = None,
    **kwargs,
) -> dict:
    if _mapper is None:  # pragma: no cover
        _mapper = dict()
    return {
        _mapper.get(key, key): value
        for key, value in kwargs.items()
        if value is not NOTHING
    }

# ------------------------------------------------------------------------------
# End of jsonpolars/sentinel.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/tests/__init__.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from .helper import run_cov_test

# ------------------------------------------------------------------------------
# End of jsonpolars/tests/__init__.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/tests/dfop_case.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl
from rich import print as rprint

from ..base_dfop import parse_dfop

if T.TYPE_CHECKING:  # pragma: no cover
    from ..dfop.api import T_DFOP


@dataclasses.dataclass
class Case:
    input_records: T.List[T.Dict[str, T.Any]] = dataclasses.field()
    dfop: "T_DFOP" = dataclasses.field()
    expected_output_records: T.List[T.Dict[str, T.Any]] = dataclasses.field()

    def run_test(self):
        print("---------- input_records ----------")
        rprint(self.input_records)
        print("---------- dfop ----------")
        rprint(self.dfop)
        df = pl.DataFrame(self.input_records)
        df1 = self.dfop.to_polars(df)
        output_records = df1.to_dicts()
        print("---------- output_records ----------")
        rprint(output_records)
        print("---------- expected_output_records ----------")
        rprint(self.expected_output_records)
        assert output_records == self.expected_output_records

        dfop_data = self.dfop.to_dict()
        print("---------- dfop_data ----------")
        rprint(dfop_data)
        dfop1 = parse_dfop(dfop_data)
        print("---------- dfop1 ----------")
        rprint(dfop1)
        df1 = self.dfop.to_polars(df)
        output_records = df1.to_dicts()
        print("---------- output_records ----------")
        rprint(output_records)
        print("---------- expected_output_records ----------")
        rprint(self.expected_output_records)
        assert output_records == self.expected_output_records

# ------------------------------------------------------------------------------
# End of jsonpolars/tests/dfop_case.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/tests/expr_case.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import dataclasses

import polars as pl
from rich import print as rprint

from ..base_expr import parse_expr

if T.TYPE_CHECKING:  # pragma: no cover
    from ..expr.api import T_EXPR


@dataclasses.dataclass
class Case:
    input_records: T.List[T.Dict[str, T.Any]] = dataclasses.field()
    expr: "T_EXPR" = dataclasses.field()
    output_records: T.List[T.Dict[str, T.Any]] = dataclasses.field()

    def run_with_columns_test(self):

        print("---------- input_records ----------")
        rprint(self.input_records)
        print("---------- expr ----------")
        rprint(self.expr)
        df = pl.DataFrame(self.input_records)
        df1 = df.with_columns(self.expr.to_polars())
        records = df1.to_dicts()
        print("---------- records ----------")
        rprint(records)
        print("---------- output_records ----------")
        rprint(self.output_records)
        assert records == self.output_records

        expr_data = self.expr.to_dict()
        print("---------- expr_data ----------")
        rprint(expr_data)
        expr1 = parse_expr(expr_data)
        print("---------- expr1 ----------")
        rprint(expr1)
        df1 = df.with_columns(expr1.to_polars())
        records = df1.to_dicts()
        print("---------- records ----------")
        rprint(records)
        print("---------- output_records ----------")
        rprint(self.output_records)
        assert records == self.output_records

# ------------------------------------------------------------------------------
# End of jsonpolars/tests/expr_case.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/tests/helper.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from ..paths import dir_project_root, dir_htmlcov
from ..vendor.pytest_cov_helper import run_cov_test as _run_cov_test


def run_cov_test(
    script: str, module: str, preview: bool = False, is_folder: bool = False
):
    _run_cov_test(
        script=script,
        module=module,
        root_dir=f"{dir_project_root}",
        htmlcov_dir=f"{dir_htmlcov}",
        preview=preview,
        is_folder=is_folder,
    )

# ------------------------------------------------------------------------------
# End of jsonpolars/tests/helper.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/typehint.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

"""
Module for type hints.

See https://github.com/pola-rs/polars/blob/main/py-polars/polars/_typing.py
"""

try:
    import typing_extensions as T
except ImportError:  # pragma: no cover
    import typing as T

if T.TYPE_CHECKING:
    from datetime import date, datetime, time, timedelta
    from decimal import Decimal

    from .expr.api import T_EXPR
    from .dfop.api import T_DFOP

# fmt: off

NumericLiteral: T.TypeAlias = T.Union[int, float, "Decimal"]
TemporalLiteral: T.TypeAlias = T.Union["date", "time", "datetime", "timedelta"]
NonNestedLiteral: T.TypeAlias = T.Union[NumericLiteral, TemporalLiteral, str, bool, bytes]
# Python literal types (can convert into a `lit` expression)
PythonLiteral: T.TypeAlias = T.Union[NonNestedLiteral, T.List[T.Any]]
# Inputs that can convert into a `col` expression
IntoExprColumn: T.TypeAlias = T.Union["T_EXPR", str]
# Inputs that can convert into an expression
IntoExpr: T.TypeAlias = T.Union[PythonLiteral, "T_EXPR", None]
# Inputs that can be interactive with +, -, *, /, etc.
OtherExpr: T.TypeAlias = T.Union[PythonLiteral, "T_EXPR"]

# selector type, and related collection/sequence
ColumnNameOrSelector: T.TypeAlias = T.Union[str, "T_EXPR"]

# fmt: on

# ------------------------------------------------------------------------------
# End of jsonpolars/typehint.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/utils_dfop.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import polars as pl

from .base_expr import BaseExpr, parse_expr
from .base_dfop import BaseDfop, parse_dfop
from .typehint import IntoExpr


if T.TYPE_CHECKING:  # pragma: no cover
    from .expr.api import T_EXPR
    from .dfop.api import T_DFOP

# ------------------------------------------------------------------------------
# End of jsonpolars/utils_dfop.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of jsonpolars/utils_expr.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import typing as T
import polars as pl

from .base_expr import BaseExpr, parse_expr
from .typehint import IntoExpr


if T.TYPE_CHECKING:  # pragma: no cover
    from .expr.api import T_EXPR


def to_jsonpolars_into_expr(expr_like: T.Union[str, dict, "T_EXPR"]) -> IntoExpr:
    if isinstance(expr_like, str):
        return expr_like
    elif isinstance(expr_like, dict):
        return parse_expr(expr_like)
    elif isinstance(expr_like, BaseExpr):
        return expr_like
    else:  # pragma: no cover
        raise NotImplementedError(f"Unsupported type: {type(expr_like)}")


def to_polars_into_expr(expr_like: T.Union[T.Any, "T_EXPR"]):
    if isinstance(expr_like, BaseExpr):
        return expr_like.to_polars()
    else:  # pragma: no cover
        return expr_like

# ------------------------------------------------------------------------------
# End of jsonpolars/utils_expr.py content
# ------------------------------------------------------------------------------