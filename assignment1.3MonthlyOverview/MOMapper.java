import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

/**
 * Created by romybeugeling on 21-09-18.
 * package private
 * output: ip   hit count
 */
class MOMapper extends Mapper<LongWritable, Text, IntWritable, Text> {
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        //split on space
        String[] parts = line.split("\\s+");

        if (parts.length < 4){
            return;
        }

        String ipAddress = parts[0];
        //get the month from the date
        String month = parts[3].substring(4, 7);

        int monthIndex = getMonthIndex(month);

        if (monthIndex == 13) {
            return;
        }

        context.write(new IntWritable(monthIndex), new Text(ipAddress));
    }


    private int getMonthIndex(String month){
        SimpleDateFormat dateFormat = new SimpleDateFormat("MMM");
        try {
            Date date = dateFormat.parse(month);
            Calendar cal = Calendar.getInstance();
            cal.setTime(date);
            return cal.get(Calendar.MONTH);
        } catch (ParseException e) {
            System.out.println("Unable to parse date: " + e);
        }
        return 12;
    }
}