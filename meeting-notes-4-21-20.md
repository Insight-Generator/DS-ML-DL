* Talked quickly about progress of webapp
  * The challenge we want to tackle is dealing with storing locally
    * Unique files, duplicate files, size restrictions, and versioning files
    * Won't tackle all of it though but a fun thought experiment
* Raymond has been tackling how to relate things
  * Discussed that we cannot just get a pair of columns as those might not be good metrics to graph blindly
  * Discussed that the model won't just take in column names as we thought and we may get the `Pearson correlation coefficient` with the full data to help give us better correlation
  * Input of model will just be the way for the model to get the CSV
  * Output will be something like an array of these set of values: `[COLUMN A, [COLUMN B, COLUMN C], WEIGHT]` as well as a cutoff value
    * What the webapp will do with these values is use the heavily weighted items and try to create graphs. The lowest weighted items will be used as a way to understand what data doesn't seem necessary
    * The returned columns may not exactly represent an X or Y axis. Instead, it will represent a set of relations. How it turns into a graph will need to be determined.