# tests/test_books.py

import pytest
from portfix.core.books import BookDB, Book

@pytest.mark.books
def test_duplicate_isbn_rejected():
    db = BookDB()
    db.add_book("123", "Title", "Author", ["Page 1"])
    with pytest.raises(ValueError):
        db.add_book("123", "Another", "Author", ["Page 1"])

@pytest.mark.books
def test_full_title_and_author():
    db = BookDB()
    book = db.add_book("456", "The Great Gatsby", "F. Scott Fitzgerald", ["Page 1"])
    assert book.title == "The Great Gatsby"
    assert book.author == "F. Scott Fitzgerald"

@pytest.mark.books
def test_empty_book_rejected():
    db = BookDB()
    with pytest.raises(ValueError):
        db.add_book("789", "Empty Book", "Nobody", [])

@pytest.mark.books
def test_get_book_by_isbn():
    db = BookDB()
    db.add_book("111", "Title", "Author", ["Page 1"])
    book = db.get_book("111")
    assert book is not None
    assert book.isbn == "111"

@pytest.mark.books
def test_get_nonexistent_book_returns_none(bookdb):
    assert bookdb.get_book("not-there") is None

@pytest.mark.books
def test_add_book_requires_pages(bookdb):
    with pytest.raises(ValueError):
        bookdb.add_book("999", "No Pages", "Nobody", [])

@pytest.mark.books
def test_get_nonexistent_book_returns_none(bookdb):
    assert bookdb.get_book("not-there") is None

@pytest.mark.books
def test_add_book_with_empty_pages_raises(bookdb):
    with pytest.raises(ValueError):
        bookdb.add_book("999", "No Pages", "Nobody", [])

@pytest.mark.books
def test_book_str_and_repr(bookdb):
    book = bookdb.add_book("123", "Title", "Author", ["Page 1"])
    s = str(book)
    r = repr(book)
    assert "Title" in s
    assert "Author" in r

@pytest.mark.books
def test_book_str_contains_title_and_author():
    book = Book("123", "The Title", "The Author", ["Page 1", "Page 2"])
    s = str(book)
    assert "The Title" in s
    assert "The Author" in s
    assert "123" in s  # ISBN should also appear

@pytest.mark.books
def test_book_repr_is_informative():
    book = Book("123", "The Title", "The Author", ["Page 1", "Page 2"])
    r = repr(book)
    # repr should include class name and key fields
    assert r.startswith("Book(")
    assert "isbn='123'" in r
    assert "title='The Title'" in r
    assert "author='The Author'" in r
    # pages count should be shown
    assert "pages=2" in r

@pytest.mark.books
def test_book_len_returns_page_count():
    book = Book("123", "The Title", "The Author", ["Page 1", "Page 2", "Page 3"])
    assert len(book) == 3

@pytest.mark.books
def test_empty_isbn_raises():
    with pytest.raises(ValueError):
        Book("", "Title", "Author", ["Page 1"])

@pytest.mark.books
def test_missing_title_or_author_raises():
    with pytest.raises(ValueError):
        Book("123", "", "Author", ["Page 1"])
    with pytest.raises(ValueError):
        Book("123", "Title", "", ["Page 1"])

@pytest.mark.books
def test_empty_pages_raises():
    with pytest.raises(ValueError):
        Book("123", "Title", "Author", [])

@pytest.mark.books
def test_turn_page_forward_and_backward():
    book = Book("123", "Title", "Author", ["Page 1", "Page 2", "Page 3"])
    # Forward
    assert book.turn_page() == "Page 2"
    # Backward
    assert book.turn_page(-1) == "Page 1"

@pytest.mark.books
def test_turn_page_invalid_direction_stays_on_page():
    book = Book("123", "Title", "Author", ["Page 1", "Page 2"])
    # At page 0, try to go back
    result = book.turn_page(-1)
    assert result == "Page 1"
    assert book.current_page == 0  # still at first page

@pytest.mark.books
def test_get_page_valid_and_invalid():
    book = Book("123", "Title", "Author", ["Page 1", "Page 2"])
    # Valid jump
    assert book.get_page(1) == "Page 2"
    assert book.current_page == 1
    # Invalid jump
    with pytest.raises(IndexError):
        book.get_page(5)
    with pytest.raises(IndexError):
        book.get_page(-1)

@pytest.mark.books
def test_all_books_returns_list():
    db = BookDB()
    b1 = db.add_book("111", "Title1", "Author1", ["Page 1"])
    b2 = db.add_book("222", "Title2", "Author2", ["Page 1"])
    books = db.all_books()
    assert b1 in books and b2 in books
    assert isinstance(books, list)