DROP TABLE IF EXISTS streamed_songs;
 
CREATE TABLE streamed_songs(artist STRING, song STRING, username STRING, ts TIMESTAMP)
ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t'
STORED AS TEXTFILE;
 
LOAD DATA LOCAL INPATH 'input.tsv' INTO TABLE streamed_songs;
