const puppeteer = require('puppeteer');
const fs = require('fs');

async function run() {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  const TEAM_NAME = '.coupon-content.more-info';

  
  try  {
    await page.goto('https://www.bovada.lv/sports/baseball/mlb?overlay=false');
    await page.screenshot({ path: 'screenshots/latest.png' });
  } catch(err) {
    console.log({err})
  }

  page.on('console' , msg => console.log(msg));
  const teamNameHandle = await page.evaluate((selector) => {
    return [...document.querySelectorAll(selector)].map((node, index) => {
      return {
        match : index,
        teamOne : {
          name : node.querySelectorAll('.name')[0].innerText,
          runline : node.querySelectorAll('.bet-price')[0].innerText.replace(/[()]/gi, ''),
          win : node.querySelectorAll('.bet-price')[2].innerText.replace(/[()]/gi, ''),
          total : node.querySelectorAll('.bet-price')[4].innerText.replace(/[()]/gi, '')
        },
        teamTwo : {
          name : node.querySelectorAll('.name')[1].innerText,
          runline : node.querySelectorAll('.bet-price')[1].innerText.replace(/[()]/gi, ''),
          win : node.querySelectorAll('.bet-price')[3].innerText.replace(/[()]/gi, ''),
          total : node.querySelectorAll('.bet-price')[5].innerText.replace(/[()]/gi, '')
        }
      }
    });
  }, TEAM_NAME);

  const jsonContent = JSON.stringify(teamNameHandle);

  fs.writeFile("output/result.json", jsonContent, 'utf8', function (err) {
    if (err) {
        console.log("An error occured while writing result to File.");
        return console.log(err);
    }
    console.log('result written to output/result.json');
  });

  await browser.close();
}

run();
