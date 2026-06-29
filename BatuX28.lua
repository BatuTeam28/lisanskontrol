-- [[ BATU SCRIPT - CHAMS WALLHACK & SAFE AIMBOT ]] --
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local Camera = workspace.CurrentCamera
local LocalPlayer = Players.LocalPlayer

-- 1. RAINBOW İMZA
local Signature = Drawing.new("Text")
Signature.Visible = true; Signature.Center = true; Signature.Outline = true
Signature.Font = 2; Signature.Size = 24
Signature.Position = Vector2.new(Camera.ViewportSize.X / 2, 30)
Signature.Text = "Matrix Premium Tg: @BatuX28 | Chams + Aimbot"

-- 2. DÜŞMAN CHAMS (Duvar Arkası Görünürlük)
local function AttachChams(p)
    if p == LocalPlayer then return end
    
    local H = Instance.new("Highlight")
    H.FillTransparency = 0.5
    H.OutlineTransparency = 0
    H.DepthMode = Enum.HighlightDepthMode.AlwaysOnTop -- Duvar arkasından göstermek için kritik
    
    p.CharacterAdded:Connect(function(char)
        task.wait(0.2)
        H.Parent = char
    end)
    if p.Character then H.Parent = p.Character end

    RunService.RenderStepped:Connect(function()
        if p.Character and p.Character:FindFirstChild("HumanoidRootPart") and p.Team ~= LocalPlayer.Team and p.Character.Humanoid.Health > 0 then
            H.Enabled = true
            H.FillColor = Color3.fromHSV(tick() % 5 / 5, 1, 1)
            Signature.Color = H.FillColor
        else
            H.Enabled = false
        end
    end)
end

for _, p in pairs(Players:GetPlayers()) do AttachChams(p) end
Players.PlayerAdded:Connect(AttachChams)

-- 3. SAFE AIMBOT (Görünen Adam)
local function GetVisibleTarget()
    local bestTarget, dist = nil, math.huge
    for _, p in pairs(Players:GetPlayers()) do
        if p ~= LocalPlayer and p.Character and p.Character:FindFirstChild("Head") and p.Team ~= LocalPlayer.Team and p.Character.Humanoid.Health > 0 then
            local pos, on = Camera:WorldToViewportPoint(p.Character.Head.Position)
            if on then
                -- Raycast ile engel kontrolü (Sadece görünenler)
                local ray = Ray.new(Camera.CFrame.Position, (p.Character.Head.Position - Camera.CFrame.Position).Unit * 500)
                local hit = workspace:FindPartOnRayWithIgnoreList(ray, {LocalPlayer.Character, Camera})
                
                if hit and hit:IsDescendantOf(p.Character) then
                    local mag = (Vector2.new(pos.X, pos.Y) - UserInputService:GetMouseLocation()).Magnitude
                    if mag < dist then bestTarget = p.Character.Head; dist = mag end
                end
            end
        end
    end
    return bestTarget
end

RunService.RenderStepped:Connect(function()
    local target = GetVisibleTarget()
    if target then
        -- Akıcı kilitlenme (Sarsıntısız)
        Camera.CFrame = Camera.CFrame:Lerp(CFrame.new(Camera.CFrame.Position, target.Position), 0.15)
    end
end)
