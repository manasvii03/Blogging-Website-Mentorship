import react, {useState} from 'react';
import API from '../../baseURL/baseURL';
function Save(){
    const [saved,setSaved]=useState(false);
    const handlesaved=async ()=>{
        try{
            const response=await API.get(`/blogs/`);
            if(!saved){
                setSaved(true);
            }
            else{
                set
            }
        }
        catch(err){
            console.log(`Error: ${err.message}`);
        }
    }
}