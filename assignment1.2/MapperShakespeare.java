import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.lib.input.FileSplit;

import java.io.IOException;

/**
 * Created by Evi on 20-9-2018.
 */
public class MapperShakespeare extends
        Mapper<LongWritable, Text, Text, Text>
{
    public void map(LongWritable key, Text value, Context context)
            throws IOException, InterruptedException {
        String fileName =  ((FileSplit) context.getInputSplit()).getPath().getName();
        String line = value.toString();
        Integer lineNumber = null;
        //loop through the lines of the text
        for (String word : line.split("\\W+")) {
            //check if there is already a line number
            if (lineNumber == null){
                lineNumber = Integer.parseInt(word);
            }else{
                context.write(new Text(word.toLowerCase()),new Text(fileName + ";" + lineNumber));
            }
        }
    }
}

