class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        # Im thinking a dict approach will work here,
        # its just checking to see if both strings have
        # the same characters

        seen = {}
        x = len(s)
        y = len(t)

        # if mismatch in length, fail immediately
        if (x != y):
            return False

        # adding all chars from str 's'
        # to our seen dict
        for i in range(x):

            # Add value association to represent count, notated by
            # how we ingest the value and associate it in loop below:
            if s[i] in seen: # if value we are currently checking on string exists
                             # exists already within out seen dict

                seen[s[i]] += 1 # increment on each additional time seen
            else:
                seen[s[i]] = 1 # this should set the value to 1 on first view, and allow us to increment

        # big difference is how we ingest at first, defining as seen[s[i]] = i
        # will just store its index in the dict, we dont want that
        #print(seen)

        # check it against other string
        for i in range(y):
            if t[i] in seen:
                # Count look up will go here, str s against str t
                # if number of occurences dont match then we will fail it.
                seen[t[i]] -= 1
                #print(seen)
                # correctly done, now we need a final check to make sure our dict counts
                # are zeroed out, and if any remains, that calls for a fail

                # if every value in the dict is 0, we can safely return true
                # if not, return false
            else:
                return False

        # This is our final check. Simply checking if all values
        # have been zeroed out by checking using a value to loop up.
        # uncomment the print statement to grasp what happens in this final step
        for i in range(len(seen)): 
            #print(seen[s[i]])
            if seen[s[i]] > 0:
                return False

        return True