import datetime
import json

class Goal():
    """This class is the core class of the program. It guides the user through
setting up a SMART Goal."""

    def __init__(self, inputs = {}):
        if inputs:
            self.input_date = inputs["input_date"]
            self.target_date = inputs["target_date"]
            self.goal = inputs["goal"]
            self.specific = inputs["specific"]
            self.measurable = inputs["measurable"]
            self.achievable = inputs["achievable"]
            self.relevant = inputs["relevant"]
            self.timely = inputs["timely"]
            self.importance = inputs["importance"]
            self.benefits = inputs["benefits"]
            self.actions = inputs["actions"]
            self.helpers = inputs['helpers']
            self.action_steps = inputs['action_steps']
        else:
            self.input_date = datetime.date.today()
            self.target_date = ''
            self.goal = ''
            self.specific = ''
            self.measurable = ''
            self.achievable = ''
            self.relevant = ''
            self.timely = ''
            self.importance = ''
            self.benefits = ''
            self.actions = []
            self.helpers = []
            self.action_steps = []
            self.cli()
        print(self.print_goal())
        with open('test.json', 'w') as f:
            f.write(self.save_goal())

    def print_goal(self):
        ret = []
        ret.append(self.print_header())
        ret.append(self.print_specific())
        ret.append(self.print_measurable())
        ret.append(self.print_achievable())
        ret.append(self.print_relevant())
        ret.append(self.print_timely())
        ret.append(self.print_importance())
        ret.append(self.print_benefits())
        ret.append(self.print_actions())
        ret.append(self.print_helpers())
        ret.append(self.print_action_steps())
        return "\n".join(ret)

    def print_header(self):
        return "%s\nStart Date: %s\t\tTarget Date: %s" % \
               (self.goal, str(self.input_date), str(self.target_date))

    def cli(self):
        print("Welcome to pygoals, a SMART Goal Setting assistant.")
        print("This is meant to be used only for significant goals, not minor tasks.")
        self.input_date = datetime.date.today()
        self.goal = input("State your goal in 1-2 sentences: ")
        print('Your goal is "' + self.goal + '".')
        while not self.target_date:
            try:
                user_target_date = input("When do you plan to finish this (YYYY-MM-DD)? ")
                self.target_date = datetime.datetime.strptime(user_target_date, '%Y-%m-%d')
            except ValueError:
                print("Incorrect date, try again.")
        print("Now, it's time to make your goal SMART.")
        print("After answering each question, you'll be given the chance to")
        print("Revise your previous answers.")
        self.edit_specific()
        self.edit_measurable()
        self.edit_achievable()
        self.edit_relevant()
        self.edit_timely()
        self.edit_importance()
        self.edit_benefits()
        self.edit_actions()
        self.edit_helpers()
        self.edit_action_steps()


    def print_specific(self):
        return "Specific: %s" % (self.specific,)

    def edit_specific(self):
        x = ''
        if self.specific:
            print("You originally said this: " + self.specific)
            print("What exactly will you accomplish? Be detailed and specific.")
            x = input("Press enter to make no changes. ")
        else:
            x = input("What exactly will you accomplish (Be detailed and specific)? ")
        if x == '':
            return True
        else:
            self.specific = x
            return True

    def print_measurable(self):
        return "Measurable: %s" % (self.measurable,)

    def edit_measurable(self):
        x = ''
        if self.measurable:
            print("You originally said this: " + self.measurable)
            print("How will you know when you have reached this goal?")
            x = input("Include deliverables and numbers. Press enter to make no changes: ")
        else:
            print("How will you know when you have reached this goal?")
            x = input("Include deliverables and numbers: ")
        if x == '':
            return True
        else:
            self.measurable = x
            return True

    def print_achievable(self):
        return "Achievable: %s" % (self.achievable,)

    def edit_achievable(self):
        x = ''
        if self.achievable:
            print("You originally said this: " + self.achievable)
            print("Is achieving this goal realistic with effort and commitment?")
            print("Have you got the resources to achieve this goal?")
            print("If not, how will you get them. Lots of detail!!!")
            x = input("Press enter to make no changes: ")
        else:
            print("Is achieving this goal realistic with effort and commitment?")
            print("Have you got the resources to achieve this goal?")
            x = input("If not, how will you get them. Lots of detail!!!")
        if x == '':
            return True
        else:
            self.achievable = x
            return True

    def print_relevant(self):
        return "Relevant: %s" % (self.relevant,)

    def edit_relevant(self):
        x = ''
        if self.relevant:
            print("You originally said this: " + self.relevant)
            print("Why is this goal significant to your life?")
            x = input("Don't be vague! Press enter to make no changes: ")
        else:
            x = input("Why is this goal significant to your life? Don't be vague! ")
        if x == '':
            return True
        else:
            self.relevant = x
            return True

    def print_timely(self):
        return "Timely: %s" % (self.timely)

    def edit_timely(self):
        x = ''
        if self.timely:
            print("You originally said this: " + self.timely)
            print("When will you achieve this goal. NOT A DATE, contextual time frame")
            x = input("Example: I will finish this before x. Press enter to make no changes: ")
        else:
            print("When will you achieve this goal. NOT A DATE, contextual time frame")
            x = input("Example: I will finish this before x: ")
        if x == '':
            return True
        else:
            self.timely = x
            return True

    def print_importance(self):
        return "This goal is important because: %s" % (self.importance)

    def edit_importance(self):
        x = ''
        if self.importance:
            print("You originally said this: " + self.importance)
            x = input("This goal is important because... Press enter to make no changes: ")
        else:
            x = input("This goal is important because... ")
        if x == '':
            return True
        else:
            self.importance = x
            return True

    def print_benefits(self):
        return "The benefits of achieving this goal will be: %s" % (self.benefits)

    def edit_benefits(self):
        x = ''
        if self.benefits:
            print("You originally said this: " + self.benefits)
            x = input("The benefits of achieving this goal will be... Press enter to make no changes: ")
        else:
            x = input("The benefits of achieving this goal will be... ")
        if x == '':
            return True
        else:
            self.benefits = x
            return True

    def print_actions(self):
        ret = []
        if self.actions:
            ret.append("These are potential obstacles and their solutions:")
            for index, action in enumerate(self.actions):
                ret.append("Action #%d\nPotential Obstacle: %s\nPotential Solutions: %s" %
                           (index, self.actions[index][0], self.actions[index][1]))
        else:
            ret.append("You haven't identified any obstacles/solutions yet.")
            ret.append("You're looking back on this 5 months from now")
            ret.append("This goal was an utter failure. Think about what went wrong.")
            ret.append("Those are your obstacles, now solve them!")
        return "\n".join(ret)

    def edit_actions(self):
        editing = True
        while editing:
            print(self.print_actions())

            print("Do you want to edit an existing action or add a new one?")
            print("To edit an action, enter it's number. To add a new one, type 'N'")
            x = input("If you are finished adding or editing, then just hit ENTER: ")
            if x:
                self.edit_action(x)
            else:
                editing = False
        return True

    def edit_action(self, x):
        editable = []
        obstacle = ''
        solutions = ''
        try:
            x = int(x)
            editable = [x, self.actions.pop(x)]
        except ValueError:
            pass
        if editable:
            print("Potential [O]bstacle")
            print(editable[1][0])
            print("Potential [S]olutions")
            print(editable[1][1])
            print("")
            print("Describe the potential obstacle, be detailed.")
            obstacle = input("Press enter to make no changes: ")
            print("")
            print("Describe the potential solutions, include specifics and resources.")
            solutions = input("Press enter to make no changes: ")
            if not obstacle and solutions:
                self.actions.insert(editable[0],[editable[1][0],editable[1][1]])
                return False
        else:
            obstacle = input("Describe the potential obstacle, be detailed. ")
            solutions = input("Describe the potential solutions, include specifics and resources. ")
        ret = []
        if editable:
            if obstacle:
                ret.append(obstacle)
            else:
                ret.append(editable[1][0])
            if solutions:
                ret.append(solutions)
            else:
                ret.append(editable[1][1])
            self.actions.insert(editable[0], ret)
        else:
            self.actions.append([obstacle, solutions])
        return True

    def print_helpers(self):
        ret = []
        if self.helpers:
            ret.append("These are the people you've identified as helpers:")
            for index, helper in enumerate(self.helpers):
                ret.append("%d: %s" % (index, helper))
        else:
            ret.append("You haven't identified any helpers yet.")
            ret.append("Remember, no man is an island!")
        return "\n".join(ret)

    def edit_helpers(self):
        editing = True
        while editing:
            print(self.print_helpers())

            print("Who are the people you will ask to help you? How will they help you?")
            print("To edit an existing helper, enter their number. To add a new helper, type 'N'")
            x = input("If you are finished, press ENTER: ")
            if x:
                self.edit_helper(x)
            else:
                editing = False
        return True

    def edit_helper(self,x):
        editable = []
        helper = ''
        try:
            x = int(x)
            editable = [x, self.helpers.pop(x)]
        except ValueError:
            pass
        if editable:
            print("You've edited this person: " + editable[1])
            print("Who will help you and how will they help you? Be specific.")
            x = input("To make no changes, press ENTER: ")
            if x:
                self.helpers.insert(editable[0],x)
                return True
            else:
                self.helpers.insert(editable[0],editable[1])
                return False
        else:
            print("Who will help you and how will they help you? Be specific.")
            x = input("Put their name first to simplify finding them: ")
            if x:
                self.helpers.append(x)
                return True
            else:
                return False

    def print_action_steps(self):
        ret = []
        if self.action_steps:
            ret.append("These are the Next Actions you've identified:")
            for index, helper in enumerate(self.action_steps):
                ret.append("Action Step #%d\nStep: %s\nEnd Date: %s" %\
              (index, self.action_steps[index][0], str(self.action_steps[index][1])))
        else:
            ret.append("You haven't identified any Next Actions You need widgets to crank.")
            ret.append("If you were going to out and do this right now, what would you do?")
        return "\n".join(ret)

    def edit_action_steps(self):
        editable = True
        while editable:
            print(self.print_action_steps())
            print("To edit an existing Action Step, enter it's number.")
            x = input("To add a new Action Step, type 'N'. When you're finished, press ENTER: ")
            if x:
                self.edit_action_step(x)
            else:
                editable = False

    def edit_action_step(self, index):
        editable = []
        action_step = []
        try:
            x = int(index)
            editable = [x, self.action_steps.pop(x)]
        except ValueError:
            pass
        if editable:
            print("You've selected this action step to edit: ")
            print("Next Action: %s" % (editable[1][0]))
            action = input("To make no changes, press ENTER: ")
            print("Completion Date: %s" % (str(editable[1][1])))
            user_date = input("Format: YYYY-MM-DD. To make no changes, press ENTER: ")
            if not action or user_date:
                self.action_steps.insert(editable[0],[editable[1]])
            else:
                act = action or editable[0]
                dte = datetime.datetime.strptime(user_date, "%Y-%m-%d") or editable[1]
                self.action_steps.insert(editable[0],[editable[0],editable[1]])
                return False
        else:
            action = input("What is the very next action to move forward on this: ")
            user_date = input("When will complete this by? (Format: YYYY-MM-DD) ")
            if action and user_date:
                try:
                    dte = datetime.datetime.strptime(user_date, "%Y-%m-%d")
                except ValueError:
                    pass
                self.action_steps.append([action, dte])
                return True
            else:
                return False

    def save_goal(self):
        return """{"__goal__":True,
        "version":'1.0',
        "goal": %s,
        "input_date": %s,
        "target_date": %s,
        "specific": %s,
        "measurable": %s,
        "achievable": %s,
        "relevant": %s,
        "timely": %s,
        "importance": %s,
        "benefits": %s,
        "actions": %s,
        "helpers": %s,
        "action_steps": %s""" % (self.goal, self.input_date, self.target_date,
                                 self.specific, self.measurable,
                                 self.achievable, self.relevant, self.timely,
                                 self.importance, self.benefits, self.actions,
                                 self.helpers, self.action_steps)

if __name__ == "__main__":
    g = Goal({"__goal__":True,"version":"1.0","goal":"goal",
              "input_date":"2016-07-18","target_date":"2016,07-19",
              "specific":"specific","measurable":"measurable",
              "achievable":"achievable","relevant":"relevant",
              "timely":"timely","importance":"importance",
              "benefits":"benefits","actions":[["obstacle","solutions"]],
              "helpers":["helper1","helper2"],
              "action_steps":[["Next Action","2016-07-18"]]})
