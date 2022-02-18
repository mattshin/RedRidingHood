const NEW_TRANSACTION = 'users/NEW_TRANSACTION';


const newTransaction = (transaction) => ({
    type: NEW_TRANSACTION,
    transaction
});



export const makeTransaction = (userid, stockid, shares, method, share_value) => async(dispatch) => {
    const transaction = await fetch (`/api/transactions/new`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            userid,
            stockid,
            shares,
            method,
            share_value
        })
    });

    if (transaction.ok) {
        const data = await transaction.json();
        dispatch(newTransaction(data));
        return null;
    } else if (transaction.status < 500) {
        const data = await transaction.json();
        if (data.errors) {
          return data.errors;
        }
      } else {
        return ["An error occurred. Please try again."];
      }

}

const initialState = {transactions: []};

export default function reducer(state = initialState, action) {

    switch (action.type) {
        case NEW_TRANSACTION:
            state.transactions.push(action.transaction)
            return state
        default:
            return state;

    }
}