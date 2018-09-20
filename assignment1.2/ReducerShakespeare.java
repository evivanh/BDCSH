import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class ReducerShakespeare
        extends Reducer<Text,Text,Text,Text> {
    //private IntWritable result = new IntWritable();

    public void reduce(Text key, Text values,
                       Context context
    ) throws IOException, InterruptedException {
//        int sum = 0;
//        for (IntWritable val : values) {
//            sum += val.get();
//        }
        //result.set(sum);
        context.write(key, values );
    }

}