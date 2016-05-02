


package com.WordToVec;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author Sameeksha Vaity (samvaity)
 *
 */

public class finalTest {

	public static void main(String[] args) throws Exception {

		BufferedReader reader = null;
		FileWriter writer = null;
		StringBuffer sb = null;
		Matcher matcher = null;

		String filePath = "G:/CodePractice/101/src/main/java/wwe/tees.txt";

		String outputFileName = "G:/CodePractice/101/Movie/Movie";

		Map<Integer, String> movieMap = new HashMap<Integer, String>();

		File file = new File(filePath);
		try {
			reader = new BufferedReader(new FileReader(file));
			String line = null;
			int movieCount = 0;
			while ((line = reader.readLine()) != null) {

				sb = new StringBuffer();

				matcher = Pattern.compile("\"([^\"]+)\"").matcher(line);
				while (matcher.find()) {
					matcher.appendReplacement(sb, matcher.group().replaceAll("\\s+", "").replaceAll(",", ""));
				}

				String s = sb.toString().replaceAll("\\[", "");

				System.out.println(s);

				movieMap.put(++movieCount, s);

			}

			System.out.println(movieMap.size());
			for (Map.Entry<Integer, String> entry : movieMap.entrySet()) {

				System.out.println(entry.getKey());

				try {
					writer = new FileWriter(new File(outputFileName + (entry.getKey()) + ".txt"));

					writer.write(entry.getValue());
				} catch (Exception e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				} finally {
					writer.close();
				}
			}

		} catch (Exception ex) {
			ex.printStackTrace();
		} finally {
			try {
				reader.close();
				writer.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}

	}
}
