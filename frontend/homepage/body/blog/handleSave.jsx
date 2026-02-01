import react, {useState} from 'react';
import API from '../../baseURL/baseURL';
import save from '../images/save.svg';
function Save({blogId}){
    const [saved,setSaved]=useState(false);
    const handleSaved=async ()=>{
        const user_token = localStorage.getItem('token');
        try{
            setSaved(!saved);
            await API.post(`/blogs/${blogId}/bookmark/`, {}, {
            headers: {
                'Authorization': `Token ${user_token}`, 
                'Content-Type': 'application/json'}});
        }
        catch(err){
            console.log(`Error: ${err.message}`);
        }
    }
    return(
        <div className="save"><button className="save" onClick={handleSaved}><svg className={saved?"saved":"notsaved"} viewBox="0 0 80 80" fill="none" height="30" width="30"><path d="M63.3333 70L40 53.3333L16.6667 70V16.6667C16.6667 14.8986 17.369 13.2029 18.6193 11.9526C19.8695 10.7024 21.5652 10 23.3333 10H56.6667C58.4348 10 60.1305 10.7024 61.3807 11.9526C62.631 13.2029 63.3333 14.8986 63.3333 16.6667V70Z"/></svg></button></div>
    );
}
export default Save;