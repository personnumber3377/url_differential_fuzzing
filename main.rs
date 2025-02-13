use url::Url;
use serde_json::json;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        eprintln!("Usage: url_parser <url>");
        return;
    }

    let input = &args[1];
    match Url::parse(input) {
        Ok(parsed_url) => {
            let result = json!({
                "valid": true,
                "scheme": parsed_url.scheme(),
                "username": parsed_url.username(),
                "password": parsed_url.password(),
                "host": parsed_url.host_str(),
                "port": parsed_url.port(),
                "path": parsed_url.path(),
                "query": parsed_url.query(),
                "fragment": parsed_url.fragment(),
            });
            println!("{}", result);
        }
        Err(_) => {
            let result = json!({ "valid": false });
            println!("{}", result);
        }
    }
}
