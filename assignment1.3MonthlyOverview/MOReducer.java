package monthlyOverview;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by romybeugeling on 21-09-18.
 * package private
 * output: ip count
 */
class MOReducer extends Reducer<IntWritable, Text, IntWritable, Text> {
    @Override
    protected void reduce(IntWritable month, Iterable<Text> values, Context context) throws IOException, InterruptedException {
        HashMap<Text, Integer> ipAddressCountMap = new HashMap<>();

        for (Text value : values) {
            if (ipAddressCountMap.containsKey(value)){
                int count = ipAddressCountMap.get(value) + 1;
                ipAddressCountMap.put(value, count);
            } else {
                ipAddressCountMap.put(value, 1);
            }
        }


        for(Map.Entry<Text, Integer> entry: ipAddressCountMap.entrySet()) {
            context.write(month, new Text(entry.getKey() + "\t" + entry.getValue()));
        }
    }
}
