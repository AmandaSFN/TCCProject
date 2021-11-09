import {createConnection} from "typeorm";

(async ()=>{
    console.log("iniciando conexão")

    await createConnection().then(connection => {
        console.log(connection.isConnected);

    }).catch(error => {
        console.error(error);
    });

})()