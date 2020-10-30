import java.util.*;



import org.eclipse.rdf4j.model.Model;
import org.eclipse.rdf4j.model.Statement;
import org.eclipse.rdf4j.model.util.ModelBuilder;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintStream;
public class Final4 {

	public static void main(String[] args) throws FileNotFoundException {
		String fileN = "C:\\CodeRep\\Sample1\\NetflixList.csv";
		String[] prop = new String[] {"show_id","type","title",
									"director","cast","country",
									"date_added","release_year","rating",
									"duration","listed_in","description"
		};
		File f = new File(fileN);
		ModelBuilder builder = new ModelBuilder();
		builder.setNamespace("sub", "http://a1Subject.org/");
		builder.setNamespace("pro", "http://a1Property.org/");
		builder.setNamespace("obj", "http://a1Object.org/");
		//Reference for writing output to a file
		//https://www.geeksforgeeks.org/redirecting-system-out-println-output-to-a-file-in-java/
		PrintStream o = new PrintStream(new File("C:\\Users\\hanum\\Desktop\\Q4_t2.ttl"));
		System.setOut(o); 
		String data;
		int i=0;
		try {
			String cols[];
			Scanner sc = new Scanner(f);
			sc.useDelimiter("\n"); 
			while(sc.hasNext()) {
				data = sc.next();
				cols=data.split(",(?=([^\"]*\"[^\"]*\")*[^\"]*$)");
				if(i>0)
				{
					//System.out.println("@@@@@@ New Row @@@@@");
//					for(int a=0;a<cols.length;a++)
//					{
//						System.out.println(cols[a]);
//					}
//					System.out.println("length of cols is: "+cols.length);
//					System.out.println("@@@@@@");
					builder.subject("sub:"+cols[0]);
					for(int j=1;j<cols.length;++j) 
					{
						if((cols[j].compareTo("")!=0)&&(j!=3 && j!=4 && j!=5 && j!=10)) 
						{
							builder.add("pro:"+prop[j],"obj:"+cols[j]);
						}
						else if((cols[j].compareTo("")!=0) && (cols[j].contains(",")))
						{
							String[] mult_cols = cols[j].split(",");
							for(int k=0;k<mult_cols.length;++k)
							{
								builder.add("pro:"+prop[j], "obj:"+mult_cols[k]);
							}
						}
						else if(cols[j].compareTo("")!=0)
						{
							builder.add("pro:"+prop[j], "obj:"+cols[j]);
						}
					}
//					System.out.println("*****Triples with movie name****");
					builder.subject("sub:"+cols[2]);
					for(int j=3;j<cols.length;++j) 
					{
						if((cols[j]!=null)&&(j!=3 && j!=4 && j!=5 && j!=10)) 
						{
							builder.add("pro:"+prop[j],"obj:"+cols[j]);
						}
						else if((cols[j]!=null) && (cols[j].contains(",")))
						{
							String[] mult_cols = cols[j].split(",");
							for(int k=0;k<mult_cols.length;++k)
							{
								builder.add("pro:"+prop[j], "obj:"+mult_cols[k]);
							}	
						}
						else if(cols[j].compareTo("")!=0)
						{
							builder.add("pro:"+prop[j], "obj:"+cols[j]);
						}
					}
				}
				i++;
				
			}
			Model model = builder.build();
			
			//for printing the model
			for(Statement st: model) {
				System.out.println(st);
			  }
			sc.close();	
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
		
	}
}


