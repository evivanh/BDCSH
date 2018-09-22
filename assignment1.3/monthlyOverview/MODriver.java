package monthlyOverview;

import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

/**
 * Created by romybeugeling on 21-09-18.
 */
public class MODriver {

    public static void main(String[] args) throws Exception {

        Job job = new Job();
        job.setJarByClass(MODriver.class);
        job.setJobName("Word Count");
        job.setNumReduceTasks(12);
        job.setPartitionerClass(MOPartitioner.class);
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        job.setMapperClass(MOMapper.class); /* Mapper */
        job.setReducerClass(MOReducer.class); /* Reducer */
        /*Intermediate key/value types: */
        job.setMapOutputKeyClass(IntWritable.class);
        job.setMapOutputValueClass(Text.class);
        /* Output value types of Reducer: */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        boolean success = job.waitForCompletion(true);
        System.exit(success ? 0 : 1);
    }
}