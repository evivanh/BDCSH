import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;


public class ReducerShakespeare
        extends Reducer<Text, Text, Text, Text>
{
    public void reduce(Text key, Iterable<Text> values, Context context)
            throws IOException, InterruptedException {
        //string builder to add the values in one string
        StringBuilder stringBuilder = new StringBuilder();
        //loop through values
        for (Text value : values) {
            //check if it is the last value so the output will be ok
            if (values.iterator().hasNext()){
                //add the value and a , to the existing values string
                stringBuilder.append(value).append(", ");
            }else {
                //add the value to the existing values string, no , because of last value
                stringBuilder.append(value);
            }
        }
        //output word and values
        context.write( key, new Text(stringBuilder.toString()));

    }
}
