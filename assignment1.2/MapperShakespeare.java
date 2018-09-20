import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.FileSplit;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;

/**
 * Created by Evi on 20-9-2018.
 */
public class MapperShakespeare extends Mapper<LongWritable, Text, Text, Text> {

//    private final static IntWritable one = new IntWritable(1);
//    private Text line = new Text();

    public void map(LongWritable key, Text value, Context context
    ) throws IOException, InterruptedException {
        String line = value.toString();
        String fileName = ((FileSplit)context.getInputSplit()).getPath().getName();
        //String[] data= line.split("\t");

        for (String word : line.split("\t")) {
            context.write(new Text(word), new Text(fileName+ " " + line));
        }

    }
}


