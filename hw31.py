import pymongo
import sys
 
def main():
    from pymongo import Connection
    connection = Connection('localhost', 27017)
    db = connection.school
    
    query = {}
    sort = [('_id',1), ('scores.score',1)]
    
    students = db.students.find(query).sort(sort)
    
    for item in students:
        remove_low_homework_score(item['scores'])
        db.students.save(item)
        
 
def remove_low_homework_score(scores):
    min_value = sys.float_info.max
    min_element = 0
 
    for lowscore in scores:
        print lowscore
        current_score = float(lowscore['score'])
        
        if lowscore['type'] == 'homework' and current_score < min_value:
                min_value = current_score
                min_element = lowscore
    
    print 'Remove homework with minimum score: ', min_element
    scores.remove(min_element)
    
main()