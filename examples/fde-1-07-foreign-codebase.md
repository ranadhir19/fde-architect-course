# Worked example — FDE 1.07: the first hour in someone else's code, annotated

Referenced by the FDE 1.07 learning session. The customer is fictional;
the reading is a composite written for this course. Annotations in
brackets name the move being made. This example uses a different
customer from the exercise, on purpose: copy the moves, not the words.

> **The room:** Larkspur Freight (from the FDE 1.04 to 1.06
> examples). A contractor's script builds the morning route
> board. The depot manager's whole symptom statement is: "some
> mornings the board is empty." The FDE has the script, no
> documentation, and a review meeting in one hour.
>
> *[The symptom is a frequency, not a failure: "some mornings"
> is the first clue. A script that always failed would empty
> the board every morning. Something conditional — a day, a
> data shape, a value that only sometimes appears — is the
> shape of cause to hunt for.]*
>
> **First move: the entry point, not the first file.** The
> script's main function is found first, and read for one
> thing only: what it calls, in what order. Three calls: load
> a settings file, read yesterday's jobs, build the board.
> Nothing else in the codebase is opened until that skeleton
> is written down.
>
> *[Fluency is triage. The skeleton tells you which files can
> possibly contain the cause — a board that is sometimes empty
> is built, or fed, conditionally — and which files cannot,
> however interesting they look.]*
>
> **The kill test:** the jobs reader skips any row whose depot
> code is blank. Most days no row is blank. The board is empty
> on exactly the mornings after a particular partner depot
> sends a file with its code column blank throughout — every
> row skipped, an empty board, and no error anywhere, because
> skipping was written as a filter, not a failure.
>
> *[The diagnosis was proved from the symptom's shape plus
> two functions. The fix proposed at the review was one line
> of prose — treat an all-blank file as an error, not an
> empty day — proposed, not applied, in the first hour.]*
>
> **The lesson:** read for the data's path, hypothesise from
> the symptom's shape, and let most of the codebase stay
> unread. The unread remainder is not ignorance; it is the
> triage that makes the hour enough.
