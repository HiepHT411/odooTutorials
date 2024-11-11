{
    "name": "Library Service",
    "summary": "Tutorial of VyNT",
    "description": """
    ====================
    It's me trying to replicate this odoo module sample
    ====================
    """,
    "author": "RyanHoag",
    "website": "hoanghiep0411",
    "category": "Services/Library",
    "version": "1.2",
    "depends": ["base"],
    "data": [
        "security/tutorial_security.xml",
        "security/ir.model.access.csv",
        "views/book_view.xml",
        "views/menu.xml",
        "views/book_list_template.xml",
        "reports/tutorial_library_book_report.xml",
        "reports/library_publisher_report.xml",
    ],
    "application": True,
    "demo": [
        "data/res.partner.csv",
        "data/tutorial.library.book.csv",
        "data/book_demo.xml",
    ],
}