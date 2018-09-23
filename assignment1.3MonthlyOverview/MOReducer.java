import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;
import java.util.Arrays;
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
        Map<String, Integer> ipAddressCountMap = new HashMap<>();

        for (Text ip : values) {
            if (ipAddressCountMap.containsKey(ip.toString())){
                int count = ipAddressCountMap.get(ip.toString()) + 1;
                ipAddressCountMap.put(ip.toString(), count);
            } else {
                ipAddressCountMap.put(ip.toString(), 1);
            }
//            context.write(month, new Text(ipAddressCountMap.keySet().toString()));
        }

        for (Entry<String, Integer> pair : ipAddressCountMap.entrySet()) {
            context.write(month, new Text(pair.getKey() + "\t" + pair.getValue()));
        }
    }
}
