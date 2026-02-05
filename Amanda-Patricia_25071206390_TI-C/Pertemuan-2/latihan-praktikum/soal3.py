tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL",
"NodeJS"}

irisan = tim_frontend.intersection(tim_backend)
backend_only = tim_backend.difference(tim_frontend)
union_skill = tim_frontend | tim_backend

print(f"Irisan: {irisan}")
print(f"Skill Tim Backend: {backend_only}")
print(f"Skill Gabungan: {union_skill}")