import random
import time

# import SlidesManager
# from library import Library
# from photo import Photo
# from slide import Slide
# import verticalPhotosManager
# from slideshow import SlideShow

start_time = time.time()
print("Start time: " + str(start_time))

fileAB = "ab_example";
fileA = "a_example";
fileB = "b_read_on";
fileC = "c_incunabula";
fileD = "d_tough_choices";
fileE = "e_so_many_books";
fileF = "f_libraries_of_the_world";

file = fileF;
f = open("inputs/" + file + ".txt", "r")

line = f.readline()
splits = line.split(' ')

TotalBooks = int(splits[0])
TotalLibs = int(splits[1])
TotalDays = int(splits[2])
RemaingDays = TotalDays

line = f.readline()
bookScores = [int(n) for n in line.split()]  # books score with ids in order

bookScoresWithIds = {}
for i in range(0, bookScores.__len__()):
    bookScoresWithIds[i] = bookScores[i]

bookScoresWithIds = {k: v for k, v in sorted(bookScoresWithIds.items(), key=lambda item: item[1], reverse=True)}
# photos = {}
# horizontalPhotos = {}
# verticalPhotos = {}
libraries = []
booksAlreadyScanned = []
librariesAlreadyScanned = []

booksInLibraries = {}
librariesBooks = {}
librariesSignUp = {}
librariesScanningCapacity = {}
librariesInitScore = {}

for i in range(0,TotalLibs):
  line = f.readline().strip()
  splits = line.split(' ')

  line = f.readline()
  bookIds = [int(n) for n in line.split()]  # books score with ids in order
  bookIds = sorted(bookIds,reverse=True) # sort the best books first

  libraryScore = 0

  for j in range(0, int(splits[1])):
      libraryScore += bookScores[j]

  for j in bookIds:
      if j in booksInLibraries.keys():
          booksInLibraries[j].append(i)
      else:
          booksInLibraries[j] = [i]

  if i in librariesBooks.keys():
      librariesBooks[i].append(bookIds)
  else:
      librariesBooks[i] = bookIds

  if i in librariesSignUp.keys():
      librariesSignUp[i].append(int(splits[1]))
  else:
      librariesSignUp[i] = int(splits[1])

  if i in librariesScanningCapacity.keys():
      librariesScanningCapacity[i].append(int(splits[2]))
  else:
      librariesScanningCapacity[i] = int(splits[2])

  if i in librariesInitScore.keys():
      librariesInitScore[i].append(libraryScore)
  else:
      librariesInitScore[i] = libraryScore

  # lib = Library(i, int(splits[0]),bookIds, int(splits[1]), int(splits[2]), libraryScore, 0)
  #
  # libraries.append(lib)
  #End of for loop

# print("Finished Reading, read " + str(N) + " photos")
# print("Now making slides for Vertical " + str(verticalPhotos.__len__()) + " photos")
# print("Vertical photos optimized, now adding them to slides")

def getLibScore(library):
    localscore = 0
    for book in librariesBooks[library]:
        if book not in booksAlreadyScanned:
            localscore += bookScores[book]
    return localscore

def getNextLibary():
    global RemaingDays
    BestScoredLibraries = {}
    for book in bookScoresWithIds.keys():
        # try:
        if book in booksInLibraries:
            libs = booksInLibraries[book]
            for library in libs:
                if library not in librariesAlreadyScanned:
                    score = getLibScore(library)
                    scanningdays = librariesScanningCapacity[library]
                    signupdays = librariesSignUp[library]
                    librarybooks = librariesBooks[library]
                    RemaingDays -= signupdays
                    # if RemaingDays>0:
                    BestScoredLibraries[library] = signupdays - scanningdays/len(librarybooks) - scanningdays*3 - (score/204421)*29
                    librariesAlreadyScanned.append(library)
        # except:
        #     print('error for book: ' + str(book))

    BestScoredLibraries = {k: v for k, v in sorted(BestScoredLibraries.items(), key=lambda item: item[1], reverse=True)}
    return BestScoredLibraries

def saveOutput(libraries, filename):
    print("Starting file output: " + filename)
    file = open("outputs/output-" + filename +".txt", "w", encoding='utf-8')

    file.write(str(libraries.__len__()) + "\n")

    for lib in libraries.keys():
        file.write(str(lib)  + ' ' + str(librariesBooks[lib].__len__()) + "\n")
        booksinlib = ' '.join(str(e) for e in librariesBooks[lib])
        file.write(booksinlib + "\n")
    file.close()
    print("Done writing file")


libraries = getNextLibary()

libraries = {k: v for k, v in sorted(libraries.items(), key=lambda item: item[1])}

saveOutput(libraries, file)


elapsed_time = time.time() - start_time

print("Total execution time: " + str(elapsed_time))