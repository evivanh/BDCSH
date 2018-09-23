import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Partitioner;

/**
 * Created by romybeugeling on 21-09-18.
 */
class MOPartitioner extends Partitioner<IntWritable, Text> {
    @Override
    public int getPartition(IntWritable month, Text ipAddress, int numOfReduceTasks) {
        return (month.get() % numOfReduceTasks);
    }
}
