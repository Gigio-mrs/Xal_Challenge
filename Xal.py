import json 

with open(r'C:\Users\co99d\OneDrive\Escritorio\xal.json') as file:
    data = json.load(file)
    sum = 0
    count = 0
    minimum = []
    old = []
    rep = []
    ans = {}
    for key in data["items"]:

        minimum.append(key["view_count"])

        old.append(key["last_activity_date"])
        
        rep.append(key["owner"]["reputation"])
        
        if "accepted_answer_id" in key:
            ans[key["owner"]["reputation"]]=key["accepted_answer_id"]
            print(key["accepted_answer_id"])

        if key["is_answered"] == False:
            count += 1
        elif key["is_answered"] == True:
            sum += key["answer_count"]
        

    print("numero de respuestas contestadas: "+ str(sum))
    print("numero de respuestas no contestadas: " + str(count))
    print("respuesta con el menor numero de vistas: " + str(min(minimum)))
    print("respuesta mas vieja: " + str(min(old)))
    print("respuesta mas nueva: " + str(max(old)))
    print("reputacion mas alta: " + str(max(rep)))
    print ("Respuesta a la reputacion mas alta: "+ str(ans[max(rep)]))
    

    