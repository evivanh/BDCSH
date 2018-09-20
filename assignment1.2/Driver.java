import java.io.IOException;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Driver {

    public static void main(String[] args) throws Exception {

//        if (args.length != 2) {
//            System.out.printf("Usage: Shakespeare <input dir> <output dir>\n");
//            System.exit(-1);
//        }

        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "Shakespeare count");
        job.setJarByClass(Driver.class);
        job.setMapperClass(MapperShakespeare.class);
        //job.setCombinerClass(ReducerShakespeare.class);
        job.setReducerClass(ReducerShakespeare.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);
        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));
        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}