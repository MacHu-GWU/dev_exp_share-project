# ==============================================================================
# Consolidated Unit Test Case Code for jsonpolars
#
# **Purpose**
#
# This document serves as a comprehensive knowledge base for the unit test
# part of the jsonpolars project,
# enabling GenAI tools to reference the entire codebase efficiently.
#
# **Rationale**
#
# Due to limitations in processing multiple files, this document concatenates
# all unit test code files into a single, easily accessible format.
#
# **Contents**
#
# - Complete unit test code from all project files
# - File paths and names preserved as comments before each file's content
#
# Note:
#
# This consolidated view is generated automatically and should be updated
# whenever significant changes are made to the project's source code.
# ==============================================================================

# ==============================================================================
# Below is the unit test code folder structure:
#
#     tests/all.py
#     tests/test_api.py
#     tests/test_dfop_aggregation.py
#     tests/test_dfop_manipulation.py
#     tests/test_expr_column.py
#     tests/test_expr_dt.py
#     tests/test_expr_function.py
#     tests/test_expr_list.py
#     tests/test_expr_manipulation.py
#     tests/test_expr_string.py
#     tests/test_expr_utils.py
#
# ==============================================================================
# ------------------------------------------------------------------------------
# Start of tests/all.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars", is_folder=True, preview=False)

# ------------------------------------------------------------------------------
# End of tests/all.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of tests/test_api.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from jsonpolars import api


def test():
    _ = api
    _ = api.parse_expr
    _ = api.T_EXPR
    _ = api.expr
    _ = api.parse_dfop
    _ = api.T_DFOP
    _ = api.dfop

    # --- expr ---
    _ = api.expr.Cast
    _ = api.expr.List
    _ = api.expr.ListGet
    _ = api.expr.Datetime
    _ = api.expr.DatetimeToString
    _ = api.expr.String
    _ = api.expr.Split
    _ = api.expr.StrJoin
    _ = api.expr.Lit
    _ = api.expr.Plus
    _ = api.expr.Minus
    _ = api.expr.Column
    _ = api.expr.Alias

    # --- dfop ---
    _ = api.dfop.Select
    _ = api.dfop.Rename
    _ = api.dfop.Drop
    _ = api.dfop.WithColumns
    _ = api.dfop.Head
    _ = api.dfop.Tail
    _ = api.dfop.Sort
    _ = api.dfop.DropNulls
    _ = api.dfop.Count


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.api", preview=False)

# ------------------------------------------------------------------------------
# End of tests/test_api.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of tests/test_dfop_aggregation.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from jsonpolars.expr import api as expr
from jsonpolars.dfop import api as dfop
from jsonpolars.tests.dfop_case import Case


case_count = Case(
    input_records=[
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ],
    dfop=dfop.Count(),
    expected_output_records=[
        {"id": 3},
    ],
)


def test():
    print("")

    case_count.run_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.dfop.aggregation", preview=False)

# ------------------------------------------------------------------------------
# End of tests/test_dfop_aggregation.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of tests/test_dfop_manipulation.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from jsonpolars.expr import api as expr
from jsonpolars.dfop import api as dfop
from jsonpolars.tests.dfop_case import Case


case_select = Case(
    input_records=[
        {"a": 1, "b": 2, "c": 3},
    ],
    dfop=dfop.Select(
        exprs=[
            "a",
            expr.Column(name="c"),
        ],
        named_exprs={
            "d": "b",
            "e": expr.Lit(value=5),
        },
    ),
    expected_output_records=[
        {"a": 1, "c": 3, "d": 2, "e": 5},
    ],
)
case_rename = Case(
    input_records=[
        {"a": 1, "b": 2, "c": 3},
    ],
    dfop=dfop.Rename(
        mapping={
            "a": "x",
            "c": "z",
        }
    ),
    expected_output_records=[
        {"x": 1, "b": 2, "z": 3},
    ],
)
case_drop = Case(
    input_records=[
        {"a": 1, "b": 2, "c": 3},
    ],
    dfop=dfop.Drop(columns=["a", expr.Column(name="c")]),
    expected_output_records=[
        {"b": 2},
    ],
)
case_with_columns = Case(
    input_records=[
        {"a": 1},
    ],
    dfop=dfop.WithColumns(
        exprs=[
            expr.Alias(
                name="b",
                expr=expr.Plus(
                    left=expr.Column(name="a"),
                    right=expr.Lit(value=1),
                ),
            ),
        ],
        named_exprs={
            "c": expr.Plus(
                left=expr.Column(name="a"),
                right=expr.Lit(value=2),
            )
        },
    ),
    expected_output_records=[
        {"a": 1, "b": 2, "c": 3},
    ],
)
case_head = Case(
    input_records=[
        {"id": 1},
        {"id": 2},
        {"id": 3},
        {"id": 4},
    ],
    dfop=dfop.Head(n=2),
    expected_output_records=[
        {"id": 1},
        {"id": 2},
    ],
)
case_tail = Case(
    input_records=[
        {"id": 1},
        {"id": 2},
        {"id": 3},
        {"id": 4},
    ],
    dfop=dfop.Tail(n=2),
    expected_output_records=[
        {"id": 3},
        {"id": 4},
    ],
)
case_count = Case(
    input_records=[
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ],
    dfop=dfop.Count(),
    expected_output_records=[
        {"id": 3},
    ],
)
case_sort_1 = Case(
    input_records=[
        {"id": 2},
        {"id": 3},
        {"id": 1},
    ],
    dfop=dfop.Sort(by=["id"]),
    expected_output_records=[
        {"id": 1},
        {"id": 2},
        {"id": 3},
    ],
)
case_sort_2 = Case(
    input_records=[
        {"id": 1, "name": "a"},
        {"id": 1, "name": "b"},
        {"id": 2, "name": "c"},
        {"id": 2, "name": "d"},
    ],
    dfop=dfop.Sort(by=["id", "name"], descending=[True, False]),
    expected_output_records=[
        {"id": 2, "name": "c"},
        {"id": 2, "name": "d"},
        {"id": 1, "name": "a"},
        {"id": 1, "name": "b"},
    ],
)
case_drop_nulls_1 = Case(
    input_records=[
        {"id": 1, "name": "a"},
        {"id": 2, "name": None},
        {"id": None, "name": "c"},
    ],
    dfop=dfop.DropNulls(),
    expected_output_records=[
        {"id": 1, "name": "a"},
    ],
)
case_drop_nulls_2 = Case(
    input_records=[
        {"id": 1, "name": "a"},
        {"id": 2, "name": None},
        {"id": None, "name": "c"},
    ],
    dfop=dfop.DropNulls(subset=["id"]),
    expected_output_records=[
        {"id": 1, "name": "a"},
        {"id": 2, "name": None},
    ],
)
case_drop_nulls_3 = Case(
    input_records=[
        {"id": 1, "name": "a"},
        {"id": 2, "name": None},
        {"id": None, "name": "c"},
    ],
    dfop=dfop.DropNulls(subset=["name"]),
    expected_output_records=[
        {"id": 1, "name": "a"},
        {"id": None, "name": "c"},
    ],
)


def test():
    print("")

    case_select.run_test()
    case_rename.run_test()
    case_drop.run_test()
    case_with_columns.run_test()
    case_head.run_test()
    case_tail.run_test()
    case_count.run_test()
    case_sort_1.run_test()
    case_sort_2.run_test()
    case_drop_nulls_1.run_test()
    case_drop_nulls_2.run_test()
    case_drop_nulls_3.run_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.dfop.manipulation", preview=False)

# ------------------------------------------------------------------------------
# End of tests/test_dfop_manipulation.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of tests/test_expr_column.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case

case_alias = Case(
    input_records=[
        {"a": 1},
    ],
    expr=expr.Alias(
        name="b",
        expr=expr.Column(name="a"),
    ),
    output_records=[
        {"a": 1, "b": 1},
    ],
)


def test():
    print("")

    case_alias.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.column", preview=False)

# ------------------------------------------------------------------------------
# End of tests/test_expr_column.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of tests/test_expr_dt.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from datetime import datetime

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case

case_datetime_to_string_1 = Case(
    input_records=[
        {"time": datetime(2024, 8, 1, 12, 30, 45)},
    ],
    expr=expr.DatetimeToString(
        expr=expr.Datetime(expr=expr.Column(name="time")),
        format="%m/%d/%Y %H:%M:%S",
    ),
    output_records=[
        {"time": "08/01/2024 12:30:45"},
    ],
)
case_datetime_to_string_2 = Case(
    input_records=[
        {"time": datetime(2024, 8, 1, 12, 30, 45)},
    ],
    expr=expr.DatetimeToString(
        expr=expr.Column(name="time"),
        format="%m/%d/%Y %H:%M:%S",
    ),
    output_records=[
        {"time": "08/01/2024 12:30:45"},
    ],
)


def test():
    print("")

    case_datetime_to_string_1.run_with_columns_test()
    case_datetime_to_string_2.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.dt", preview=False)

# ------------------------------------------------------------------------------
# End of tests/test_expr_dt.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of tests/test_expr_function.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case


case_plus_1 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.Plus(
        left=expr.Column(name="id"),
        right=expr.Lit(value=100),
    ),
    output_records=[
        {"id": 101},
    ],
)
case_plus_2 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.Plus(
        left=expr.Column(name="id"),
        right=100,
    ),
    output_records=[
        {"id": 101},
    ],
)
case_minus_1 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.Minus(
        left=expr.Column(name="id"),
        right=expr.Lit(value=100),
    ),
    output_records=[
        {"id": -99},
    ],
)
case_minus_2 = Case(
    input_records=[
        {"id": 1},
    ],
    expr=expr.Minus(
        left=expr.Column(name="id"),
        right=100,
    ),
    output_records=[
        {"id": -99},
    ],
)


def test():
    print("")

    case_plus_1.run_with_columns_test()
    case_plus_2.run_with_columns_test()
    case_minus_1.run_with_columns_test()
    case_minus_2.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.function", preview=False)

# ------------------------------------------------------------------------------
# End of tests/test_expr_function.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of tests/test_expr_list.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case


case_list_get_1 = Case(
    input_records=[
        {"lst": [1, 2]},
    ],
    expr=expr.ListGet(
        expr=expr.Column(name="lst"),
        index=0,
        # index=expr.Lit(value=1),
    ),
    output_records=[
        {"lst": 1},
    ],
)

case_list_get_2 = Case(
    input_records=[
        {"lst": [1, 2]},
    ],
    expr=expr.ListGet(
        expr=expr.List(expr=expr.Column(name="lst")),
        index=expr.Lit(value=1),
    ),
    output_records=[
        {"lst": 2},
    ],
)


def test():
    print("")

    case_list_get_1.run_with_columns_test()
    case_list_get_2.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.list", preview=False)

# ------------------------------------------------------------------------------
# End of tests/test_expr_list.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of tests/test_expr_manipulation.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from datetime import datetime

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case

case_cast = Case(
    input_records=[
        {"time": "2024-08-01T12:30:45"},
    ],
    expr=expr.Cast(
        dtype=pl.Datetime(),
        expr=expr.Column(name="time"),
    ),
    output_records=[
        {"time": datetime(2024, 8, 1, 12, 30, 45)},
    ],
)


def test():
    print("")

    case_cast.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.manipulation", preview=False)

# ------------------------------------------------------------------------------
# End of tests/test_expr_manipulation.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of tests/test_expr_string.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import polars as pl

from jsonpolars.expr import api as expr
from jsonpolars.tests.expr_case import Case


case_split_1 = Case(
    input_records=[
        {"id": "a-1"},
    ],
    expr=expr.Split(
        expr=expr.Column(name="id"),
        by="-",
    ),
    output_records=[
        {"id": ["a", "1"]},
    ],
)

case_split_2 = Case(
    input_records=[
        {"id": "a-1"},
    ],
    expr=expr.Split(
        expr=expr.String(expr=expr.Column(name="id")),
        by="-",
    ),
    output_records=[
        {"id": ["a", "1"]},
    ],
)

case_join = Case(
    input_records=[
        {"foo": "1"},
        {"foo": "2"},
        {"foo": "3"},
    ],
    expr=expr.StrJoin(
        delimiter="-",
        expr=expr.Column(name="foo"),
    ),
    output_records=[
        {"foo": "1-2-3"},
        {"foo": "1-2-3"},
        {"foo": "1-2-3"},
    ],
)


def test():
    print("")

    case_split_1.run_with_columns_test()
    case_split_2.run_with_columns_test()
    case_join.run_with_columns_test()


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.string", preview=False)

# ------------------------------------------------------------------------------
# End of tests/test_expr_string.py content
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# Start of tests/test_expr_utils.py content
# ------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import polars as pl
from jsonpolars.expr import api as expr
from jsonpolars.utils_expr import (
    to_jsonpolars_into_expr,
    to_polars_into_expr,
)


def test_to_jsonpolars_into_expr():
    assert to_jsonpolars_into_expr("col_1") == "col_1"
    assert to_jsonpolars_into_expr({"type": "column", "name": "col_1"}) == expr.Column(
        name="col_1"
    )
    assert to_jsonpolars_into_expr(expr.Column(name="col_1")) == expr.Column(
        name="col_1"
    )


def test_to_polars_into_expr():
    assert to_polars_into_expr("col_1") == "col_1"
    assert isinstance(to_polars_into_expr(expr.Column(name="col_1")), pl.Expr)


if __name__ == "__main__":
    from jsonpolars.tests import run_cov_test

    run_cov_test(__file__, "jsonpolars.expr.utils", preview=False)

# ------------------------------------------------------------------------------
# End of tests/test_expr_utils.py content
# ------------------------------------------------------------------------------