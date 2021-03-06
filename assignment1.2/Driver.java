import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Driver {

    public static void main(String[] args) throws Exception {

        if (args.length != 2) {
            System.out.printf("Usage: Shakespeare <input dir> <output dir>\n");
            System.exit(-1);
        }

        Job job = new Job();
        job.setJarByClass(Driver.class);
        job.setJobName("Word Count");
        FileInputFormat.setInputPaths(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        job.setMapperClass(MapperShakespeare.class); /* Mapper */
        job.setReducerClass(ReducerShakespeare.class); /* Reducer */
/*Intermediate key/value types: */
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(Text.class);
/* Output value types of Reducer: */
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(Text.class);
        boolean success = job.waitForCompletion(true);
        System.exit(success ? 0 : 1);
    }
}