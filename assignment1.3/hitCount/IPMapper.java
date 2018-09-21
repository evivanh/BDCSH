package hitCount;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

/**
 * Created by romybeugeling on 21-09-18.
 * package private
 * output: ip   hit count
 */
class IPMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        //split on space
        String[] parts = line.split("\\s+");

        if (parts.length > 0){
            context.write(new Text(parts[0]), new IntWritable(1));
        }
    }
}