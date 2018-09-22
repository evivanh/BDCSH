import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;
import java.io.IOException;


public class ReducerShakespeare
        extends Reducer<Text, Text, Text, Text>
{
    public void reduce(Text key, Iterable<Text> values, Context context)
            throws IOException, InterruptedException {
        StringBuilder stringBuilder = new StringBuilder();
        for (Text value : values) {
            if (values.iterator().hasNext()){
                stringBuilder.append(value).append(", ");
            }else {
                stringBuilder.append(value);
            }
        }
        context.write( key, new Text(stringBuilder.toString()));

    }
}
//if (groupedWords.containsKey(key)){
//        ArrayList<Text> wordValues = groupedWords.get(key);
//        wordValues.add(value);
//        }else{
//        ArrayList<Text> wordValues = new ArrayList<>();
//        wordValues.add(value);
//        groupedWords.put(key, wordValues);
//
//        }
//
//        for (Map.Entry<Text,ArrayList<Text>> entry : groupedWords.entrySet()) {
//        Text wordKey = entry.getKey();
//        ArrayList<Text> placeValue = entry.getValue();
//        for (int i = 0; i <placeValue.size() ; i++) {
//        stringBuilder.append(placeValue.get(i));
//        }
//        context.write( wordKey, new Text(stringBuilder.toString()));
//        }