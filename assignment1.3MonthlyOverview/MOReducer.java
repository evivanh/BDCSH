import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Iterator;

/**
 * Created by romybeugeling on 21-09-18.
 * package private
 * output: ip count
 */
class MOReducer extends Reducer<IntWritable, Text, IntWritable, Text> {
    @Override
    protected void reduce(IntWritable month, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        Map<Text, Integer> ipAddressCountMap = new HashMap<>();

        for (Text value : values) {
            context.write(month, value);
            if (ipAddressCountMap.containsKey(value)){
                int count = ipAddressCountMap.get(value) + 1;
                ipAddressCountMap.put(value, count);
            } else {
                ipAddressCountMap.put(value, 1);
            }
        }

//        for (Entry<Text, Integer> pair : ipAddressCountMap.entrySet()) {
//            context.write(month, new Text(pair.getKey() + "\t" + pair.getValue()));
//        }
    }
}
