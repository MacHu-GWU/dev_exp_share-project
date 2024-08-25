Leverage GenAI For Code Writing
==============================================================================
This blog post explores how to use Generative AI (GenAI) to produce functional code snippets that align with a specific codebase's project characteristics and personal style. We'll delve into the use of knowledge bases and few-shot learning techniques.

This blog is hosted at: https://dev-exp-share.readthedocs.io/en/latest/search.html?q=Leverage+GenAI+For+Code+Writing&check_keywords=yes&area=default


Sample Use Case
------------------------------------------------------------------------------
Let's consider a practical example using my jsonpolars library (https://github.com/MacHu-GWU/jsonpolars-project). This library allows users to write DataFrame manipulation logic using JSON, providing a programming language-agnostic interface. In jsonpolars, all Polars expressions and DataFrame methods are abstracted into Python class objects with JSON serialization interfaces. However, with over 200 Polars expressions, manual implementation would be time-consuming. My approach was to establish the code framework and design patterns myself, then provide GenAI with a few-shot examples to generate the remaining code.


Train AI with the Knowledge Base
------------------------------------------------------------------------------
To begin, I created an automated script to extract key code from the library and consolidate it into a knowledge base. Here's an example of such a script:

.. dropdown:: generate_knowledge_base.py

    .. literalinclude:: ./generate_knowledge_base.py
       :language: python
       :linenos:

The resulting knowledge base text includes the codebase structure and source code for each module:

.. dropdown:: source_code_knowledge_base.py

    .. literalinclude:: ./source_code_knowledge_base.py
       :language: python
       :linenos:

.. dropdown:: test_cases_knowledge_base.py

    .. literalinclude:: ./test_cases_knowledge_base.py
       :language: python
       :linenos:


Generate a Narrative Description
------------------------------------------------------------------------------
Next, I used AI to generate an introductory text for the codebase. The prompt was:

.. dropdown:: prompt

    ``jsonpolars`` is A Python library that enables writing Polars data manipulation logic using JSON syntax.

    Please use the project knowledge information to write an introduction to this project, no more than 1000 words.

下面是生成的 Instruction:

.. dropdown:: generated instruction

    Thank you for providing that additional information. I'll incorporate it into the description. Here's an updated introduction to the jsonpolars project, including the new details:

    jsonpolars is an innovative Python library designed to bridge the gap between JSON-based data manipulation syntax and the powerful Polars data processing library. This project aims to provide a flexible and intuitive way to express Polars operations using JSON structures, making it easier for developers to work with Polars in various contexts.

    Key features of jsonpolars include:

    1. JSON-based expression of Polars operations: The library allows users to define complex data transformations using JSON syntax, which can then be translated into native Polars operations.

    2. Object-oriented representation of Polars operations: jsonpolars converts each Polars DataFrame method and expression into a corresponding Python class. This approach provides a structured way to represent Polars operations in a JSON-compatible format.

    3. Serialization and deserialization: Each class in jsonpolars provides a `from_dict` method to deserialize it from a Python dictionary and a `to_dict` method to serialize it back to a dictionary. This enables easy conversion between JSON representations and Python objects.

    4. Polars integration: The most crucial method for each class is `to_polars`, which converts the jsonpolars object into the corresponding Polars method or expression. This allows seamless integration with existing Polars workflows.

    5. Support for DataFrame operations (dfop): jsonpolars implements various DataFrame operations such as select, rename, drop, with_columns, head, tail, sort, and drop_nulls. These operations can be expressed in JSON format and executed on Polars DataFrames.

    6. Expression handling (expr): The library provides support for column operations, datetime manipulations, literal values, arithmetic operations, list operations, type casting, and string functions. These expressions can be combined to create complex transformations.

    7. Extensible architecture: jsonpolars is designed with extensibility in mind, allowing for easy addition of new operations and expressions as the Polars library evolves.

    8. Type hinting and documentation: jsonpolars includes comprehensive type hints and documentation to aid developers in understanding and using the library effectively.

    The project structure includes separate modules for DataFrame operations (dfop) and expressions (expr), as well as utility functions and type definitions. It also includes a testing framework to ensure the correctness of the JSON-to-Polars conversions.

    jsonpolars can be particularly useful in scenarios where data processing pipelines need to be defined in a language-agnostic manner, such as in distributed systems or when working with configuration-driven data transformations. By allowing users to express Polars operations in JSON, the library enables greater flexibility in how data processing logic is stored, transmitted, and executed.

    The object-oriented approach of jsonpolars, combined with its serialization and deserialization capabilities, provides a robust foundation for working with Polars operations in a JSON-compatible format. This design allows for easy manipulation, storage, and transmission of data processing logic, while the `to_polars` method ensures that these operations can be efficiently executed using the native Polars library.

    While the library is still in its early stages (version 0.1.1), it shows promise in simplifying the integration of Polars into JSON-centric ecosystems and providing a new approach to defining data manipulation workflows. The combination of JSON compatibility and direct Polars integration makes jsonpolars a powerful tool for developers working with data processing pipelines in Python.


Generating Source Code and Test Cases
------------------------------------------------------------------------------
With the instruction and knowledge base in place, we can now instruct the AI to generate code that strictly adheres to the project's coding style. Here's an example prompt:

.. dropdown:: prompt

    .. code-block:: markdown

        Based on the project knowledge, including how I write the source code and how I write the unit test, help me write the corresponding Python class implementation and Unit Test code for polars.Expr.dt.year method.

        The polars expression document is at https://docs.pola.rs/api/python/stable/reference/expressions/api/polars.Expr.dt.year.html.

        Below is the corresponding polars document from their official website:

        ```python
        def year(self) -> Expr:
            """
            Extract year from underlying Date representation.

            Applies to Date and Datetime columns.

            Returns the year number in the calendar date.

            Returns
            -------
            Expr
                Expression of data type :class:`Int32`.

            Examples
            --------
            >>> from datetime import date
            >>> df = pl.DataFrame(
            ...     {"date": [date(1977, 1, 1), date(1978, 1, 1), date(1979, 1, 1)]}
            ... )
            >>> df.with_columns(
            ...     calendar_year=pl.col("date").dt.year(),
            ...     iso_year=pl.col("date").dt.iso_year(),
            ... )
            shape: (3, 3)
            ┌────────────┬───────────────┬──────────┐
            │ date       ┆ calendar_year ┆ iso_year │
            │ ---        ┆ ---           ┆ ---      │
            │ date       ┆ i32           ┆ i32      │
            ╞════════════╪═══════════════╪══════════╡
            │ 1977-01-01 ┆ 1977          ┆ 1976     │
            │ 1978-01-01 ┆ 1978          ┆ 1977     │
            │ 1979-01-01 ┆ 1979          ┆ 1979     │
            └────────────┴───────────────┴──────────┘
            """
        ```

.. dropdown:: AI Generated Source Code and Test Case

    .. code-block:: markdown

        Certainly! I'll create the corresponding Python class implementation for `polars.Expr.dt.year` method and its unit test based on the project structure and coding style you've shown.

        First, let's implement the `DtYear` class in the `jsonpolars/expr/dt.py` file:

        ```python
        # -*- coding: utf-8 -*-

        import typing as T
        import dataclasses

        import polars as pl

        from ..sentinel import NOTHING, REQUIRED, OPTIONAL
        from ..base_expr import ExprEnum, BaseExpr, expr_enum_to_klass_mapping, parse_expr

        if T.TYPE_CHECKING:  # pragma: no cover
            from .api import T_EXPR

        @dataclasses.dataclass
        class DtYear(BaseExpr):
            type: str = dataclasses.field(default=ExprEnum.dt_year.value)
            expr: "T_EXPR" = dataclasses.field(default=REQUIRED)

            @classmethod
            def from_dict(cls, dct: T.Dict[str, T.Any]):
                return cls(expr=parse_expr(dct["expr"]))

            def to_polars(self) -> pl.Expr:
                return ensure_datetime(self.expr).year()

        expr_enum_to_klass_mapping[ExprEnum.dt_year.value] = DtYear
        ```

        Now, let's add the corresponding unit test in the `tests/test_expr_dt.py` file:

        ```python
        # -*- coding: utf-8 -*-

        from datetime import date

        import polars as pl

        from jsonpolars.expr import api as expr
        from jsonpolars.tests.expr_case import Case

        case_dt_year = Case(
            input_records=[
                {"date": date(1977, 1, 1)},
                {"date": date(1978, 1, 1)},
                {"date": date(1979, 1, 1)},
            ],
            expr=expr.DtYear(
                expr=expr.Column(name="date"),
            ),
            output_records=[
                {"date": 1977},
                {"date": 1978},
                {"date": 1979},
            ],
        )

        def test():
            print("")

            # ... (existing test cases)

            case_dt_year.run_with_columns_test()

        if __name__ == "__main__":
            from jsonpolars.tests import run_cov_test

            run_cov_test(__file__, "jsonpolars.expr.dt", preview=False)
        ```

        To complete the implementation, you'll need to make a few more changes:

        1. Add `DtYear` to the `ExprEnum` class in `jsonpolars/base_expr.py`:

        ```python
        class ExprEnum(str, enum.Enum):
            # ... (existing enums)
            dt_year = "dt_year"
            # ... (other enums)
        ```

        2. Update the `T_EXPR` type alias in `jsonpolars/expr/api.py`:

        ```python
        T_EXPR = T.Union[
            # ... (existing types)
            DtYear,
            # ... (other types)
        ]
        ```

        3. Import `DtYear` in `jsonpolars/expr/api.py`:

        ```python
        from .dt import DtYear
        ```

        These changes will integrate the new `DtYear` class into your existing `jsonpolars` structure, following the patterns established in your project. The unit test case demonstrates how to use the `DtYear` expression and verifies its functionality by comparing the output with the expected results.


Test the Generated Code
------------------------------------------------------------------------------
After generating the code, the next step is to test it to ensure it functions correctly within the existing codebase.

- Source code: https://github.com/MacHu-GWU/jsonpolars-project/blob/main/jsonpolars/expr/dt.py
- Unit test: https://github.com/MacHu-GWU/jsonpolars-project/blob/main/tests/test_expr_dt.py
