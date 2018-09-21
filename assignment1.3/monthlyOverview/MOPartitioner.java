package monthlyOverview;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;

/**
 * Created by romybeugeling on 21-09-18.
 */
class MOPartitioner extends Partitioner<Text, IntWritable> {
    @Override
    public int getPartition(Text text, IntWritable intWritable, int numOfReduceTasks) {
        //return same number as month start with 0
        //maand als key gebruiken als key vanuit mapper
        //return key.get()
        return 0;
    }
}
