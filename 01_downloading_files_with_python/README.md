## Exercise #1 - Downloading Files with Python.

#### Problems Statement

You need to download 10 files that are sitting at the following specified
`HTTP` urls. You will use the `Python` package `requests` to do this
work.

You will need to pull the filename from the download uri.

The files are `zip` files that will also need to be unzipped into
their `csv` format.

They should be downloaded into a folder called `downloads` which
does not exist currently inside the `Exercise-1` folder. You should
use `Python` to create the directory, do not do it manually.

Generally, your script should do the following ...

1. create the directory `downloads` if it doesn't exist
2. download the files one by one.
3. split out the filename from the uri, so the file keeps its
   original filename.
4. Each file is a `zip`, extract the `csv` from the `zip` and delete
   the `zip` file.
5. For extra credit, download the files in an `async` manner using the
   `Python` package `aiohttp`. Also try using `ThreadPoolExecutor` in
   `Python` to download the files. Also write unit tests to improve your skills. --**To Do
