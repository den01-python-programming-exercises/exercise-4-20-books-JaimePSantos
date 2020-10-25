from book import Book
def main():
    bookList = []
    while(True):
      bookTitle = input("Title: ")
      bookPages = int(input("Pages: "))
      bookPubYear = int(input("Publication year: "))
      if not bookTitle:
        break
      bookList.append(Book(bookTitle,bookPages,bookPubYear))
    whatToPrint = input("What information will be printed?")
    for book in bookList:
      if(whatToPrint=="everything"):
        print(book)
      elif(whatToPrint=="name"):
        print(book.name)
        
if __name__ == '__main__':
    main()
