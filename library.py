class Library:
    def __init__(self, id, booksIds, signupDays, canScanBooks, libraryScore):
        self.id = id
        self.totalBooks = len(booksIds)
        self.booksIds = booksIds
        self.signupDays = signupDays
        self.canShipBooks = canScanBooks
        self.libraryScore = libraryScore
        self.daysToComplete = len(booksIds)/canScanBooks + signupDays