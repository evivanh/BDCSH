import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

/**
 * Created by romybeugeling on 21-09-18.
 */
public class IPDriver {

    public static void main(String[] args) throws Exception {

        Job job = new Job();
        job.setJarByClass(IPDriver.class);
        job.setJobName("Hit Count");
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        job.setMapperClass(IPMapper.class); /* Mapper */
        job.setReducerClass(IPReducer.class); /* Reducer */
        /*Intermediate key/value types: */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);
        /* Output value types of Reducer: */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        boolean success = job.waitForCompletion(true);
        System.exit(success ? 0 : 1);
    }
}