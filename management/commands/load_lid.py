import os
import csv
from lid.models import Match
from django.core.management.base import BaseCommand, CommandError
import datetime

class Command(BaseCommand):
    args = 'Model.csv'
    help = 'Import `Model`.csv into `Model` database.'

    def handle(self, *args, **options):
#        for obj in Match.objects.all():
#            obj.delete()
#        print("deleted everything")
        now = str(datetime.datetime.now()) 
        with open('/djangoproject/usatdata/lid/Similarities_(model_to_bill).csv') as f:
            reader = csv.reader(f)
            next(reader)
            print("about to start importing. This may take awhile")
            weirdos = []
            for row in reader:
                print("evaluating " + str(row[24]) + " " + str(row[25]))
                if Match.objects.filter(enabled=row[0], simtype=row[1], actualleg=row[2], modelid=row[3], simid=row[4], view=row[5], maxwordscore=row[6], fiveplusscore=row[7], tenplusscore=row[8], lidscore=row[9], maxwords=row[10], fiveplus=row[11], tenplus=row[12], fifteenplus=row[13], exactmatch=row[14], modelwords=row[15], number=row[16], modeltext=row[17], modelname=row[18], modeltype=row[19], modelcat=row[20], modelsubject=row[21], modeldesc=row[22], year1=row[23], state=row[24], billno=row[25], party=row[26], statusdate=row[27], noideawhathisis=row[28], primarysponsors=row[30], cosponsors=row[31], othersponsors=row[32], billtext="0", billtitle=row[34], billid=row[35], textid=row[36]).count() > 0:
                    print( "already exists, continuing")
                    continue
                else:              
                    print("New record, adding")
                    Match.objects.create(enabled=row[0], simtype=row[1], actualleg=row[2], modelid=row[3], simid=row[4], view=row[5], maxwordscore=row[6], fiveplusscore=row[7], tenplusscore=row[8], lidscore=row[9], maxwords=row[10], fiveplus=row[11], tenplus=row[12], fifteenplus=row[13], exactmatch=row[14], modelwords=row[15], number=row[16], modeltext=row[17], modelname=row[18], modeltype=row[19], modelcat=row[20], modelsubject=row[21], modeldesc=row[22], year1=row[23], state=row[24], billno=row[25], party=row[26], statusdate=row[27], noideawhathisis=row[28], primarysponsors=row[30], cosponsors=row[31], othersponsors=row[32], billtext="0", billtitle=row[34], billid=row[35], textid=row[36], timestamp=now)
                    weirdos.append(row)
        print("imported everything. here are you weirdos:")
        print(weirdos)
#        deletecounter = 0
#        for row in Match.objects.all():
#            if Match.objects.filter(modelid=row.modelid, state=row.state, billno=row.billno, year1=row.year1).count() >1:
#                row.delete()
#                deletecounter+=1
#                print("deleted "+ str(deletecounter) + "total records")  



#        with open('/djangoproject/usatdata/lid/Similarities_(model_to_bill).csv', 'rb') as in_file, open('/djangoproject/usatdata/lid/deduped_similarities.csv', 'wb') as out_file:
#            seen = set()
#            for line in in_file:
#                if line not in seen:
#                    seen.add(line)
#                    out_file.write(line)

        
            
            
