import random
import time

start_time = time.time()
print("Start time: " + str(start_time))

fileAB = "ab_example";
fileA = "a_example";
fileB = "b_read_on";
fileC = "c_incunabula";
fileD = "d_tough_choices";
fileE = "e_so_many_books";
fileF = "f_libraries_of_the_world";

file = fileE;
f = open("inputs/" + file + ".txt", "r")

print("Analyzing: " + str(file))

line = f.readline()
splits = line.split(' ')

TotalBooks = int(splits[0])
TotalLibs = int(splits[1])
TotalDays = int(splits[2])
RemaingDays = TotalDays

print("Total Books: " + str(TotalBooks))
print("Total Libraries: " + str(TotalLibs))
print("Total Days: " + str(TotalDays))

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

libsumBooks = 0
bookscoresum = 0
maxscore = 0
minscore = 0

for k,bookids in librariesBooks.items():
    libsumBooks += len(bookids)
    s = getLibScore(k)
    if maxscore < s:
        maxscore = s
    if minscore > s:
        minscore = s
    bookscoresum += s

averageBooks = libsumBooks/TotalLibs
averageLibScore = bookscoresum/TotalLibs

print("Average Books in Libraries: " + str(averageBooks))
print("Average Library Score: " + str(averageLibScore))

print("Min Library Score: " + str(minscore))
print("Max Library Score: " + str(maxscore))

signupdays = 0
scanningdays = 0

for k,v in librariesSignUp.items():
    signupdays += v
signupdays = signupdays/TotalLibs

for k,v in librariesScanningCapacity.items():
    scanningdays += v
scanningdays = scanningdays/TotalLibs

print("Average Signup Days for a Library: " + str(signupdays))
print("Average Scanning Day for a Library: " + str(scanningdays))

# libraries = getNextLibary()
#
# libraries = {k: v for k, v in sorted(libraries.items(), key=lambda item: item[1])}
#
# saveOutput(libraries, file)


elapsed_time = time.time() - start_time

print("Total execution time: " + str(elapsed_time))