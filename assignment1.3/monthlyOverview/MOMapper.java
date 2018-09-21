package monthlyOverview;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * Created by romybeugeling on 21-09-18.
 * package private
 * output: ip   hit count
 */
class MOMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        //split on space
        String[] parts = line.split("\\s+");

        if (parts.length < 4){
            return;
        }

        String ipAddress = parts[0];
        String monthYear = parts[4].substring(3, 11);

        Date d = getDate(monthYear);




        //part four = 3 tot 11
        if (parts.length > 0){
            context.write(new Text(parts[0]), new IntWritable(1));
        }
    }


    private Date getDate(String monthYear){
        SimpleDateFormat dateFormat = new SimpleDateFormat("MMM/yyyy");

        try {
            return dateFormat.parse(monthYear);
        } catch (ParseException e) {
            System.out.println("Unable to parse date: " + e);
        }
        return null;
    }
}