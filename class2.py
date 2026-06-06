# Source - https://stackoverflow.com/q/11619942
# Posted by user1546721, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-04, License - CC BY-SA 4.0

# Source - https://stackoverflow.com/a/11620052
# Posted by Igor Chubin, modified by community. See post 'Timeline' for change history
# Retrieved 2026-05-04, License - CC BY-SA 
n=123
rev=0
while n>0:
    digit=n%10
    rev=rev+digit
    n//=10
print(rev)

