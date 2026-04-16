# ══════════════════════════════════════════════════════
#  SAMPLE DATA — Copy this to test your functions
# ══════════════════════════════════════════════════════

sample_students = [
    {
        "name": "Alice Johnson",
        "scores": [85, 92, 78, 95, 88],
        "subject": "Math",
        "year": 2023
    },
    {
        "name": "Bob Smith",
        "scores": [72, 68, 75, 70, 73],
        "subject": "Science",
        "year": 2023
    },
    {
        "name": "Charlie Brown",
        "scores": [95, 98, 92, 97, 94],
        "subject": "Math",
        "year": 2024
    },
    {
        "name": "Diana Prince",
        "scores": [88, 85, 90, 87, 89],
        "subject": "English",
        "year": 2023
    },
    {
        "name": "Eve Adams",
        "scores": [76, 82, 79, 81, 78],
        "subject": "Science",
        "year": 2024
    },
]
def laod_data(*records):
 Valid_records=[]
 required_fields=["name", "scores", "subject", "year"]
 for record in records:
    if not isinstance(record,dict):
       print("error, this is not a dictionary")
       continue  

    elif not all(feilds in record for feilds in required_fields):
        print("missing required fields")
        continue

    elif not isinstance(record,["scores"],list):
       print("record skipped")
       continue

    elif not len(record["scores"])==0:
       print("record skipped")
       continue

    Valid_records.append(record)

 return Valid_records

print(laod_data())


def calculate_stats(data,**options): 
 include_min = options.get("include_min", True)
 include_max = options.get("include_max", True)
 include_avg = options.get("include_avg", True)
 decimal_places = options.get("decimal_places", 2)

 if len(data) == 0:
   return {"error": "No data provided", "count": 0}   

 all_avg=[sum(s["scores"]) / len(s["scores"]) for s in data]

 stats={"count":len(data)}
 if include_avg:
   stats["avgerage_score"]=round(sum(all_avg)/len(all_avg),decimal_places)
 if include_min:
   stats["avgerage_min"]=round(min(all_avg),decimal_places)
 if include_max:
   stats["avgerage_max"]=round(max(all_avg),decimal_places)

 return data

def filter_studne(data,**criteria):
 min_avg = criteria.get("min_avg", 0)
 subject = criteria.get("subject")
 year    = criteria.get("year")
 

 result=data
 result={s for s in result
         if sum(s["scores"]) / len(s["scores"]) >= min_avg}
 if subject:
   result={s for s in result
          if s["subject"].lower()==subject.lower()}
   
 if year:
   result={s for s in result
           if s["year"]==year}
 print(f"[filter] {len(result)}/{len(data)} students match")

 return result


def transform_data(data, *transformations):
    """Apply named transforms: normalize, round_scores, add_grade."""
    import copy
    data = copy.deepcopy(data)  

    all_avgs = [sum(s["scores"]) / len(s["scores"]) for s in data]
    max_avg  = max(all_avgs) if all_avgs else 1

    def normalize(student):
        avg = sum(student["scores"]) / len(student["scores"])
        student["normalized"] = round(avg / max_avg * 100, 2)
        return student

    def round_scores(student):
        student["scores"] = [round(s) for s in student["scores"]]
        return student

    def add_grade(student):
        avg = sum(student["scores"]) / len(student["scores"])
        student["grade"] = ("A" if avg>=90 else "B" if avg>=75
                             else "C" if avg>=60 else "D")
        return student

    dispatch = {"normalize": normalize,
                "round_scores": round_scores,
                "add_grade": add_grade}

    for name in transformations:
        fn = dispatch.get(name)
        if not fn:
            print(f"[warn] Unknown transform: {name}")
            continue
        data = [fn(s) for s in data]
        print(f"[transform] Applied '{name}'")
    return data

def generate_report(data, sort_by="name", top_n=None, show_stats=True):
   
    def avg(s): return sum(s["scores"]) / len(s["scores"])

    key_fn = avg if sort_by == "avg" else lambda s: s["name"]
    reverse = sort_by == "avg"
    sorted_data = sorted(data, key=key_fn, reverse=reverse)
    if top_n:
        sorted_data = sorted_data[:top_n]

    print("\n===== STUDENT REPORT =====")
    for s in sorted_data:
        a = round(avg(s), 2)
        grade = s.get("grade", "N/A")
        norm  = s.get("normalized", "-")
        print(f"  {s['name']:<15} {s['subject']:<10}"
              f" yr={s['year']}  avg={a}  grade={grade}"
              f"  norm={norm}")

    if show_stats:
        stats = calculate_stats(data)
        print(f"\n  Stats → {stats}")
    print("==========================")
    return sorted_data

def pipeline(data, *steps, **config):
    """Run data through a sequence of processing steps.
    Each step must be callable and accept + return a list."""
    verbose = config.get("verbose", True)

    if verbose:
        print(f"[pipeline] Starting with {len(data)} records")

    result = data
    for step in steps:
        if not callable(step):
            print(f"[pipeline] Skipping non-callable: {step}")
            continue
        if verbose:
            print(f"[pipeline] → {step.__name__}")
        result = step(result)

    if verbose:
        print(f"[pipeline] Done. {len(result)} records out.")
    return result
