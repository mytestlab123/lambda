// Code: https://gist.github.com/JonnyDavies/dcca4b369d9bf6a6c19d9f5d2363df75

let response;

exports.lambdaHandler = async (event, context) => {
    const EMPLOYEES = [
        { 'name' : 'bob',  'empolyee_id' : 1},
        { 'name' : 'jeff', 'empolyee_id' : 2},
        { 'name' : 'fred', 'empolyee_id' : 3},
        { 'name' : 'joe',  'empolyee_id' : 4}
    ];
    
    try {
        // Log to view full Http request in Cloudwatch
        console.log(event);

        let result = '';

        if (event.routeKey === 'GET /employee') {
            let start = 0; let end = EMPLOYEES.length;

            if (event.queryStringParameters){
                if (event.queryStringParameters.start >= 0){
                    start = event.queryStringParameters.start
                }
                if (event.queryStringParameters.end <= EMPLOYEES.length){
                    end = event.queryStringParameters.end
                }
            }
            if (start < end) {
                result = JSON.stringify(EMPLOYEES.slice(start, end));
            } else {
                result = JSON.stringify(EMPLOYEES.slice(0, EMPLOYEES.length)); 
            }
        } 
        else if (event.routeKey === 'POST /employee') {
            EMPLOYEES.push(JSON.parse(event.body));
            result = JSON.stringify(EMPLOYEES);
        }
        else if (event.routeKey === 'GET /employee/{id}'){
            result = JSON.stringify(EMPLOYEES.find(e => e.empolyee_id == event.pathParameters.id));
        }
        response = {
            'statusCode': 200,
            'body': JSON.stringify({
                message: result,
            })
        }
    } catch (err) {
        console.log(err);
        return err;
    }

    return response
};