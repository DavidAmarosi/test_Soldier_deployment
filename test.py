from operator import itemgetter

def Sort_the_list_by_distance(list_soldier: list[dict]) -> list[dict]:
    list_soldier_by_distance = sorted(list_soldier, key=itemgetter("distance"),reverse=True)
    return list_soldier_by_distance


def residential_house(soldiers: list[dict])-> list[dict]:
    house_1 = [[] for row in range(10)]
    house_2 = [[] for row in range(10)]
    index = 0
    Embedded_list = []
    List_of_non_embedded = []
    for soldier in soldiers:
        if index < 80:
            soldier.update({"house": "house_1","room": index // 8})
            # soldier.room = index // 8
            Embedded_list.append(soldier)

        if index < 160:
            soldier.update({"house": "house_2","room": (index-80) // 8})
            # soldier.house = "house_2"
            # soldier.room = (index-80) // 8
            Embedded_list.append(soldier)

        else:
            soldier.update({"status":"waiting list"})
            List_of_non_embedded.append(setattr)

        index +=1

    return len(Embedded_list),len(List_of_non_embedded)

residential_house(Sort_the_list_by_distance([{"soder_nomber":8525125,"first_name":"ron","last_name":"b","gender":"male","city":"asdod","distance":10},        
        {"soder_nomber":8841961,"first_name":"roni","last_name":"c","gender":"female","city":"beer_sheva","distance":5}]))


