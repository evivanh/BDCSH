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
            if (ipAddressCountMap.containsKey(value)){
                int count = ipAddressCountMap.get(value) + 1;
                ipAddressCountMap.put(value, count);
            } else {
                ipAddressCountMap.put(value, 1);
            }
        }

        Iterator<Entry<Text, Integer>> iterator = ipAddressCountMap.entrySet().iterator();
        while (iterator.hasNext()) {
            Map.Entry<Text, Integer> pair = (Map.Entry<Text, Integer>) iterator.next();
//            System.out.println(pair.getKey() + " = " + pair.getValue());
            context.write(month, new Text(pair.getKey() + "\t" + pair.getValue()));
        }
//
//            for(Map.Entry<Text, Integer> entry: ipAddressCountMap.entrySet()) {
//            context.write(month, new Text(entry.getKey() + "\t" + entry.getValue()));
//        }
    }
}
