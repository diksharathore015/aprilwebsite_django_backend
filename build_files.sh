echo "BUILD START"
python 3.10 -m pip install -r requirement.tsx
python 3.10 manage.py collectstatic --noinput --clear
echo "BUILD END"