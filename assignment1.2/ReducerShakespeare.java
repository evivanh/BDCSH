import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;


public class ReducerShakespeare
        extends Reducer<Text, Text, Text, Text>
{
    public void reduce(Text key, Iterable<Text> values, Context context)
            throws IOException, InterruptedException {
        StringBuilder stringBuilder = new StringBuilder();
        //loop through values
        for (Text value : values) {
            //check if it the last value so the output will be ok
            if (values.iterator().hasNext()){
                stringBuilder.append(value).append(", ");
            }else {
                stringBuilder.append(value);
            }
        }
        context.write( key, new Text(stringBuilder.toString()));

    }
}
