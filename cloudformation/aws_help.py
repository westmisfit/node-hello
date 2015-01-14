#!/usr/bin/python

import sys, time, json, traceback
import boto.cloudformation

conn = boto.cloudformation.connect_to_region("us-east-1")

complete_status = (
    "CREATE_COMPLETE", "ROLLBACK_COMPLETE", 
    "DELETE_FAILED", "DELETE_COMPLETE", 
    "ROLLBACK_FAILED", "ROLLBACK_COMPLETE",
    "UPDATE_COMPLETE", "UPDATE_ROLLBACK_FAILED", "UPDATE_ROLLBACK_COMPLETE")

def find_stack(stack_name):
    try:
        stacks = conn.describe_stacks(stack_name_or_id=stack_name)
        return stacks[0]
    except:
        return None

def create_stack(stack_name):
    stack = find_stack(stack_name)
    if stack != None:
        print "Stack [" + stack_name + "] already exists, status: " + stack.stack_status
        # _update_stack(stack_name)
    else:
        _create_stack(stack_name)


def update_stack(stack_name):
    stack = find_stack(stack_name)
    if stack != None:
        if stack.stack_status == "ROLLBACK_COMPLETE":
            print "Stack [" + stack_name + "] is rollbacked, delete it and create it again."
        else:
            _update_stack(stack_name)
    else:
        print "Stack [" + stack_name + "] not exists"


def delete_stack(stack_name):
    stack = find_stack(stack_name)
    if stack != None:
        _delete_stack(stack.stack_id)
    else:
        print "Stack [" + stack_name + "] not exists"


def _wait_for(stack_id, success_status, fail_status=complete_status):
    last_status = ""
    stack = None
    while stack == None or stack.stack_status not in complete_status:
        time.sleep(1)
        stack = find_stack(stack_id)
        if stack.stack_status == last_status:
            sys.stdout.write(".")
            sys.stdout.flush()
        else:
            if last_status != "":
                print ""
            sys.stdout.write(stack.stack_status)
            sys.stdout.flush()
            last_status = stack.stack_status
    print ""
    if last_status != success_status:
        raise Exception, (
            "Failed. expected status '" + success_status + "', " +
            "but now is '" + last_status + "'")

def _load_template_body(stack_name):
    template_body = open("templates/" + stack_name + ".template.json", "r").read()
    return template_body

def _load_parameters(stack_name):
    parameters = open("templates/" + stack_name + ".parameters.json", "r").read()
    items = json.loads(parameters)
    # print items
    items = list(map(lambda item: (item["ParameterKey"], item["ParameterValue"]), items))
    # print items
    return items

def _create_stack(stack_name):
    template_body = _load_template_body(stack_name)
    parameters    = _load_parameters(stack_name)
    try:
        stack_id = conn.create_stack(stack_name=stack_name,
            template_body=template_body,
            parameters=[
                ("KeyName", "west")
            ])
        print stack_id
        _wait_for(stack_id, "CREATE_COMPLETE")
    except:
        print "Stack [" + stack_name + "] did not created."
        traceback.print_exc()
    else:
        print "Stack [" + stack_name + "] created."

def _update_stack(stack_name):
    template_body = _load_template_body(stack_name)
    parameters    = _load_parameters(stack_name)
    try:
        stack_id = conn.update_stack(stack_name=stack_name,
            template_body=template_body,
            parameters=[
                ("KeyName", "west")
            ])
        print stack_id
        _wait_for(stack_id, "UPDATE_COMPLETE")
    except:
        print "Stack [" + stack_name + "] did not updated."
        traceback.print_exc()
    else:
        print "Stack [" + stack_name + "] updated."

def _delete_stack(stack_id):
    try:
        conn.delete_stack(stack_name_or_id=stack_id)
        _wait_for(stack_id, "DELETE_COMPLETE")
    except:
        print "Stack [" + stack_id + "] did not deleted."
        traceback.print_exc()
    else:
        print "Stack [" + stack_id + "] deleted."


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", type=str, choices=["create-stack", "update-stack", "delete-stack"], help="operations")
    parser.add_argument("stack_name", type=str, help="cloudformation stack name")
    args = parser.parse_args()
    #print args

    if args.operation == "create-stack":
        create_stack(args.stack_name)
    elif args.operation == "update-stack":
        update_stack(args.stack_name)
    elif args.operation == "delete-stack":
        delete_stack(args.stack_name)

